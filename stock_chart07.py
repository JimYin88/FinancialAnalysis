# Created on Jun 9, 2022
#
# @author: Jim Yin


from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from datetime import datetime as dt
import pandas_datareader as pdr
import yfinance as yf
from dash.dependencies import State
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from datetime import date, timedelta


def get_stock_price_fig(df):

    fig1 = go.Figure(data=go.Ohlc(x=df.index,
                                  open=df['Open'],
                                  high=df['High'],
                                  low=df['Low'],
                                  close=df['Close']),
                                  layout_xaxis_rangeslider_visible=False)
    return fig1
    

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([html.H1(children="Welcome to the Stock Chart App!", 
                               style={'textAlign': 'center', 'color': 'blue'},
                               className="start"),
                       
                       
                       html.Div([html.P("Input stock ticker: "),
                                 html.Div([dcc.Input(id="dropdown_tickers", type="text"),
                                           ],
                                           className="form")],
                                 className="input-place"),
                       
                       html.Div([html.P("Input date range: "),
                                 dcc.DatePickerRange(id='my-date-picker-range',
                                                     min_date_allowed=dt(1995, 8, 5),
                                                     max_date_allowed=dt.now(),
                                                     initial_visible_month=dt.now(),
                                                     start_date = dt.now().date() - timedelta(days=5*365),
                                                     end_date=dt.now().date())
                                                     ],
                                                     className="date"),
                       
                       html.Div([html.Button("Click to plot stock chart", 
                                             className="stock-btn", 
                                             id="stock"),
                                 ]),
                       
                       html.Div([html.Div([], id="graphs-content")],
                                className="content"),
                       ],
                       className="container")


# callback for stocks graphs
@app.callback([Output("graphs-content", "children"),], 
              [Input("stock", "n_clicks"),
               Input('my-date-picker-range', 'start_date'),
               Input('my-date-picker-range', 'end_date')],
              [State("dropdown_tickers", "value")])
def stock_price(n, start_date, end_date, val):
    if n == None:
        return [""]
        #raise PreventUpdate
    if val == None:
        raise PreventUpdate
    else:
        # if start_date != None:
            # df = yf.download(val, str(start_date), str(end_date))
        df = pdr.get_data_yahoo(val, start_date, end_date)
            
        # else:
        #     df = yf.download(val, str(start_date), str(end_date))
            # df = pdr.get_data_yahoo(val, start_date, end_date)
            
     
    df['MA50'] = df['Close'].rolling(50).mean()
    df['MA200'] = df['Close'].rolling(200).mean() 
            
    fig1 = go.Figure(data=[go.Ohlc(x=df.index,
                                  open=df['Open'],
                                  high=df['High'],
                                  low=df['Low'],
                                  close=df['Close'],
                                  name=f"OHLC Chart",),
                           go.Scatter(x=df.index,
                                      y=df['MA50'],
                                      name="50-day moving average",
                                      line=dict(color='blue', width=2)),
                           go.Scatter(x=df.index,
                                      y=df['MA200'],
                                      name="200-day moving average",
                                      line=dict(color='red', width=2))])
    
    fig1.update(layout_xaxis_rangeslider_visible=False)
    fig1.update_layout(title=f"Stock Chart of {val.upper()}",
                       xaxis_title="Date",
                       yaxis_title="Stock Price",
                       title_x = 0.5,
                       font=dict(family="Times Roman",
                                 size=24,
                                 color="black"))
                       
    # print(type([dcc.Graph(figure=fig1)]))
    return [dcc.Graph(figure=fig1)]


if __name__ == '__main__':
    app.run_server(debug=False)

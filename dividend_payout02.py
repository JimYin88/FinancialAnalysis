# Created on Jun 9, 2022
#
# @author: Jim Yin


from datetime import datetime as dt
import yfinance as yf
from dash.dependencies import State
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from datetime import date, timedelta
from dash import Dash, dcc, html, dash_table, Input, Output
from dash.dash_table import DataTable, FormatTemplate


money = FormatTemplate.money(4)


app = Dash(__name__)


app.layout = html.Div([html.H1(children='Dashboard by Dash',
                               style={'textAlign': 'center', 'color': 'blue'},
                               className="start"),
                       
                       html.Div([html.P("Input stock ticker: "),
                                 html.Div([dcc.Input(id="dropdown_tickers", type="text"),
                                           ],
                                           className="form")],
                                 className="input-place"),
                                            
                       html.Div([html.Button("Click to show history of dividend payment", 
                                             className="stock-btn", 
                                             id="stock"),
                                 ]),
                       
                       html.Div([html.Div([], id="graphs-content")],
                                 className="content"),
                       ],
                       className="container")


@app.callback([Output("graphs-content", "children")], 
              [Input("stock", "n_clicks")],
              [State("dropdown_tickers", "value")])
def dividend_payout(n, val):

    if n == None:
        return [""]
        #raise PreventUpdate
    if val == None:
        raise PreventUpdate
    else:
        df = yf.Ticker(val)
        df.history(period="30y")
        df1 = df.actions
        df1 = df1.drop('Stock Splits', axis = 1)
        df1 = df1.reset_index()
        df1 = df1[df1['Dividends'] != 0]
        df1['Date'] = df1['Date'].dt.strftime('%m/%d/%Y')
        
        fig1 = DataTable(id='datatable_interactivity',
                                 columns=[dict(name='Date', id='Date'),
                                          dict(name='Dividends', id='Dividends', type='numeric', format=money)],
                                 data=df1.to_dict('records'),
                                 style_cell={'textAlign': 'center', 'color': 'black', 'fontSize':20, 'font-family':'Times Roman'},
                                 page_action="native",
                                 page_current= 0,
                                 page_size= 15)
    
    return [fig1]


if __name__ == '__main__':
    app.run_server(debug=True)
    

'''
Created on Jun 7, 2022

@author: Jim Yin
'''

from dash import Dash, html, dcc, Input, Output, dash_table
# import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
# import pandas as pd
# import pandas_datareader as pdr
# import datetime as dt
import yfinance as yf

stock_ticker = "MSFT"
msft = yf.Ticker(stock_ticker)


# get historical market data
msft_stock_price = msft.history(period="2y")
msft_stock_price['MA50'] = msft_stock_price['Close'].rolling(50).mean()
msft_stock_price['MA200'] = msft_stock_price['Close'].rolling(200).mean()


fig1 = go.Figure(data=[go.Ohlc(x=msft_stock_price.index,
                               open=msft_stock_price['Open'],
                               high=msft_stock_price['High'],
                               low=msft_stock_price['Low'],
                               close=msft_stock_price['Close'],
                               name="OHLC Chart",),
                       go.Scatter(x=msft_stock_price.index, 
                                  y=msft_stock_price['MA50'], 
                                  name="50-day moving average", 
                                  line=dict(color='blue', width=2)),
                       go.Scatter(x=msft_stock_price.index, 
                                  y=msft_stock_price['MA200'], 
                                  name="200-day moving average", 
                                  line=dict(color='red', width=2))])

fig1.update(layout_xaxis_rangeslider_visible=False)

# Instantiate our App and incorporate BOOTSTRAP theme stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div(children=[
    html.H1(children='Dashboard by Dash', style={'textAlign': 'center', 'color': 'blue'}),

    html.H2(children=f'A chart of {stock_ticker} stock price'),
     
    dcc.Graph(
        id='example-graph01',
        figure=fig1)
])



if __name__ == '__main__':
    app.run_server(debug=False)




# go.Scatter(x=df.time, y=df.MA20, line=dict(color='green', width=1))])


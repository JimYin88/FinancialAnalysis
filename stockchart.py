# This module retrieve stock prices for AAPL and MSFT plots Dash stock charts.
# Created on May 1, 2022
#
# @author: Jim Yin


from dash import Dash, html, dcc, Input, Output, dash_table
# import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
# import pandas as pd
import pandas_datareader as pdr
import datetime as dt


start = dt.datetime(2017, 1, 1)
end = dt.datetime(2021, 12, 31)

aapl_df = pdr.get_data_yahoo('AAPL', start, end)


fig1 = go.Figure(data=go.Ohlc(x=aapl_df.index,
                    open=aapl_df['Open'],
                    high=aapl_df['High'],
                    low=aapl_df['Low'],
                    close=aapl_df['Close']),
                    layout_xaxis_rangeslider_visible=False)


msft_df = pdr.get_data_yahoo('MSFT', start, end)

fig2 = go.Figure(data=go.Ohlc(x=msft_df.index,
                    open=msft_df['Open'],
                    high=msft_df['High'],
                    low=msft_df['Low'],
                    close=msft_df['Close']),
                    layout_xaxis_rangeslider_visible=False)


# Instantiate our App and incorporate BOOTSTRAP theme stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.H2(children='A chart of AAPL stock price'),
     
    dcc.Graph(
        id='example-graph01',
        figure=fig1),
        
    html.H2(children='A chart of MSFT stock price'),

    dcc.Graph(
        id='example-graph02',
        figure=fig2)
])



if __name__ == '__main__':
    app.run_server(debug=False)



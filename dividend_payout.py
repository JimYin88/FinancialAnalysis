# Created on Jun 7, 2022
#
# @author: Jim Yin


from dash import Dash, dcc, html, dash_table, Input, Output
# import plotly.express as px
# import pandas as pd
import yfinance as yf
from dash.dash_table import DataTable, FormatTemplate


ticker = "MSFT"
msft = yf.Ticker(ticker)

# get stock info
# print(msft.info)

# get historical market data
# hist = msft.history(period="10y")


msft.history(period="20y")

# show actions (dividends, splits)
df1 = msft.actions

df1 = df1.drop('Stock Splits', axis = 1)
df1 = df1.reset_index()
df1 = df1[df1['Dividends'] != 0]
df1['Date'] = df1['Date'].dt.strftime('%m/%d/%Y')

money = FormatTemplate.money(2)

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Dashboard by Dash', style={'textAlign': 'center', 'color': 'blue'}),
    
    html.H2(children=f'{ticker} Dividend Payout', style={'textAlign': 'center', 'color': 'black'}),
    
    DataTable(
        id='datatable-interactivity',
        columns=[dict(name='Date', id='Date'),
                 dict(name='Dividends', id='Dividends', type='numeric', format=money)],
        data=df1.to_dict('records'),
        # editable=True,
        # filter_action="native",
        # sort_action="native",
        # sort_mode="multi",
        # column_selectable="single",
        # row_selectable="multi",
        # row_deletable=True,
        # selected_columns=[],
        # selected_rows=[],
        style_cell={'textAlign': 'center', 'color': 'black', 'fontSize':20, 'font-family':'Times Roman'},
        page_action="native",
        page_current= 0,
        page_size= 10,
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
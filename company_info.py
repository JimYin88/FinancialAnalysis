'''
Created on Jun 7, 2022

@author: Jim Yin
'''


from dash import Dash, dcc, html, dash_table, Input, Output
# import plotly.express as px
import pandas as pd
import yfinance as yf
from dash.dash_table import DataTable, FormatTemplate


ticker = "MSFT"
msft = yf.Ticker(ticker)

info_list = pd.DataFrame([[k, msft.get_info()[k]] for k in msft.get_info()])
info_list.columns = ['Header', 'Info']
info_list = info_list[info_list['Header'] != 'companyOfficers']


app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Dashboard by Dash', style={'textAlign': 'center', 'color': 'blue'}),
    
    html.H2(children=f'{ticker}: Company Profile', style={'textAlign': 'center', 'color': 'black'}),
    
    DataTable(
        id='datatable-interactivity',
        columns=[dict(name='Header', id='Header', type='text'),
                 dict(name='Info', id='Info', type='text')],
        data=info_list.to_dict('Records'),
        style_data={'whiteSpace': 'normal',
                    'height': 'auto',},
        # editable=True,
        filter_action="native",
        style_cell_conditional=[
            {'if': {'column_id': 'Header'},
             'width': '25%'},
            {'if': {'column_id': 'Info'},
             'width': '65%'},
            ],
        # sort_action="native",
        # sort_mode="multi",
        # column_selectable="single",
        # row_selectable="multi",
        # row_deletable=True,
        # selected_columns=[],
        # selected_rows=[],
        style_cell={'textAlign': 'left', 
                    'color': 'black', 
                    'fontSize':16, 
                    'font-family':'Times Roman'},
        page_action="native",
        page_current= 0,
        page_size= 12,
    )
])


if __name__ == '__main__':
    app.run_server(debug=False)
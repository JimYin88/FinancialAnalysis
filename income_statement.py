# Created on May 7, 2022
#
# @author: Jim Yin

from yahoofinancials import YahooFinancials
import pandas as pd

ticker = 'AAPL'
yf = YahooFinancials(ticker)

income_statement = yf.get_financial_stmts ('annual', 'income')

aapl_is = income_statement['incomeStatementHistory']['AAPL']

df_list = []

for d in aapl_is:
    df_list.append(pd.DataFrame.from_dict(d, orient='index'))
    
df_is = pd.concat(df_list)

print(df_is)

balance_statement = yf.get_financial_stmts('annual', 'balance')

aapl_bs = balance_statement['balanceSheetHistory']['AAPL']

df_list = []

for d in aapl_bs:
    df_list.append(pd.DataFrame.from_dict(d, orient='index'))

df_bs = pd.concat(df_list)

print(df_bs)


cash_flow = yf.get_financial_stmts('annual', 'cash')
aapl_cf = cash_flow['cashflowStatementHistory']['AAPL']

df_list = []

for d in aapl_cf:
    df_list.append(pd.DataFrame.from_dict(d, orient='index'))

df_cf = pd.concat(df_list) 

print(df_cf)

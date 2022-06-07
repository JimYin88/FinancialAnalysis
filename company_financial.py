'''
Created on Jun 7, 2022

@author: Jim Yin
'''

import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info
print(msft.info)

msft_earnings = msft.get_earnings()
print(msft_earnings)




# get historical market data
hist = msft.history(period="1y")
print(hist.head())

print(hist.shape)


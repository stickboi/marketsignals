import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = yf.download("GOOG AAPL", period="1y")

#print(data.head())
td = (data["Close"]["AAPL"]- data["Close"]["GOOG"]).to_frame()

td["tdma"] = td[0].rolling(20).mean()
td["bu"] = td["tdma"]+2*td["tdma"].rolling(20).std()
td["bl"] = td["tdma"]-2*td["tdma"].rolling(20).std()
td.dropna(inplace = True)

plot = td.plot()
plt.show()
print(td)
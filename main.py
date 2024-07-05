import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = yf.download("GOOG AAPL", period="1y")
data.to_csv("data.csv")
#print(data.head())
td = (data["Close"]["AAPL"]- data["Close"]["GOOG"]).to_frame()

td["tdma"] = td[0].rolling(20).mean()
td["std"] = td[0].rolling(20).std(ddof=0)
td["bu"] = td["tdma"]+2*td["std"]
td["bl"] = td["tdma"]-2*td["std"]
#td["np-std"] = td[0].rolling(20).apply(np.std)
#td["pd-std"] = td[0].rolling(20).std(ddof=0)

plot = td.plot()
plt.show()
print(td)
td.to_csv("td.csv")

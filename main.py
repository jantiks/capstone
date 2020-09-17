import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df_tesla = pd.read_csv("Tesla_Stock.csv",index_col="Date", parse_dates=True)
df_ford = pd.read_csv("Ford_Stock.csv",index_col="Date",parse_dates=True)
df_gm = pd.read_csv("GM_Stock.csv",index_col="Date", parse_dates=True)
# df_tesla["Open"].plot()
# df_ford["Open"].plot()
# df_gm["Open"].plot()
# plt.legend(["tesla","ford","gm"])
# plt.show()
# df_tesla["Volume"].plot()
# df_ford["Volume"].plot()
# df_gm["Volume"].plot()
# plt.legend(["Tesla","Ford","GM"])
# plt.show()
# print(df_ford["Volume"].idxmax())
# df_tesla["Total Traded"] = df_tesla["Open"]*df_tesla["Volume"]
# df_ford["Total Traded"] = df_ford["Open"]*df_ford["Volume"]
# df_gm["Total Traded"] = df_gm["Open"]*df_gm["Volume"]
# df_tesla["Total Traded"].plot()
# df_ford["Total Traded"].plot()
# df_gm["Total Traded"].plot()
# plt.legend(["Tesla","Ford","Gm"])
# plt.show()
# print(df_tesla["Total Traded"].idxmax())
# df_tesla["MA50"] = df_tesla["Open"].rolling(50).mean()
# df_tesla["MA200"] = df_tesla["Open"].rolling(200).mean()
# df_tesla["Open"].plot(figsize=(16,6))
# df_tesla["MA50"].plot()
# df_tesla["MA200"].plot()
# plt.legend(["Open","MA50","MA200"])
# plt.show()
# from pandas.plotting import scatter_matrix
# df_scater = pd.DataFrame()
# df_scater["Tesla open"] = df_tesla['Open']
# df_scater["Ford open"] = df_ford["Open"]
# df_scater["Gm open"] = df_gm["Open"]
# scatter_matrix(df_scater)
# plt.show()
df_tesla["Returns"] = ((df_tesla["Close"])/df_tesla["Close"].shift(periods=1)) - 1
df_ford["Returns"] = ((df_ford["Close"])/df_ford["Close"].shift(periods=1)) - 1
df_gm["Returns"] = ((df_gm["Close"])/df_gm["Close"].shift(periods=1)) - 1
# df_tesla["Returns"].hist(bins=100)
# df_ford["Returns"].hist(bins=100)
# df_gm["Returns"].hist(bins=100)
# plt.legend(["tesla","ford","gm"])
# print(df_tesla.head())
# plt.show()
# df_tesla["Returns"].plot.box()
# df_ford["Returns"].plot.box()
# df_gm["Returns"].plot.box()
# plt.legend(["tesla","ford","gm"])
# plt.show()
# df_tesla["daily_cumulative_return"] = ( 1 + df_tesla["Returns"] ).cumprod()
# df_ford["daily_cumulative_return"] = ( 1 + df_ford["Returns"] ).cumprod()
# df_gm["daily_cumulative_return"] = ( 1 + df_gm["Returns"] ).cumprod()
# df_tesla["daily_cumulative_return"].plot()
# df_ford["daily_cumulative_return"].plot()
# df_gm["daily_cumulative_return"].plot()
# plt.show()
# df_gm["Camulative returnes"] = df_gm["Close"]
# for i in range(0,df_gm.index.size):
#     df_gm["Camulative returnes"][i] = df_gm["Close"][i] / df_gm["Close"][0]
# print(df_gm)
# df_tesla["Camulative returnes"] = df_tesla["Returns"]
# for i in range(0,df_tesla.index.size):
#     df_tesla["Camulative returnes"][i] = df_tesla["Close"][i] / df_tesla["Close"][0]
# print(df_tesla)

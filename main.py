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
df_tesla["MA50"] = df_tesla["Open"].rolling(50).mean()
df_tesla["MA200"] = df_tesla["Open"].rolling(200).mean()
df_tesla["Open"].plot(figsize=(16,6))
df_tesla["MA50"].plot()
df_tesla["MA200"].plot()
plt.legend(["Open","MA50","MA200"])
plt.show()


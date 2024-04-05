import pandas as pd

df = pd.read_excel('movieinfo.xlsx')
print(df.info())
df = df.dropna()
print(df.info())
df.to_excel('./movieinfo_nona.xlsx', index=False)


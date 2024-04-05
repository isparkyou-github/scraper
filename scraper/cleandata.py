import pandas as pd

df = pd.read_excel('./movieinfo_nona.xlsx')

def clean_data(x):
    return x[:x.find(' ')]

df['电影名字'] = df['电影名字'].apply(clean_data)
df['时长'] = df['时长'].apply(clean_data)
df['上映时间'] = df['上映时间'].apply(clean_data)

df.to_excel('./movieinfo_cleaned.xlsx', index=False)


import pandas as pd

df = pd.read_excel('movieinfo_cleaned.xlsx')
print(df[df['分数'] > df['分数'].mean()][['电影名字', '分数']])

def includeChina(x):
    return '中国' in x
def includeJapan(x):
    return '日本' in x

print(df[(df['国家'].apply(includeChina) | df['国家'].apply(includeChina)) & (df['分数'] > df['分数'].mean())][['电影名字', '国家', '分数']])



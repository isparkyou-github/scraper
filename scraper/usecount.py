import pandas as pd

df = pd.read_excel('movieinfo_cleaned.xlsx')

def getYear(x):
    return int(x[:4])

print(df[df['上映时间'].apply(getYear) >= 2000]['上映时间'].count())

print(df['上映时间'].groupby(df['上映时间'].apply(getYear)).count())

import pandas as pd

df = pd.read_excel('movieinfo_cleaned.xlsx')
print(df['时长'].argmax())
print(df['时长'].max())
print(df.iloc[df['时长'].argmax(), :])

#print(df['时长'].argmin())
#print(df['时长'].max())
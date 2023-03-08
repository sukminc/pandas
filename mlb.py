import pandas as pd

df = pd.read_csv('mlb-player-stats-Batters.csv')

print(df.head())
print(df.shape)
print(df.describe())
print(df.info())
print(df.drop_duplicates())
# print(df.fillna(value))
# print(df.astype(type))

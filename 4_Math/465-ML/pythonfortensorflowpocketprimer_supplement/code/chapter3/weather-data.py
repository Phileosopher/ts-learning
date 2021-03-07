import pandas as pd

df = pd.read_csv("weather_data.csv")
print(df)
print(df.shape)  # rows, columns 
print(df.head()) # df.head(3)
print(df.tail())
print(df[1:3])
print(df.columns)
print(type(df['day']))
print(df[['day','temperature']])
print(df['temperature'].max())


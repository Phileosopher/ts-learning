import pandas as pd
 
df = pd.read_csv("Housing.csv")
 
minimum_bdrms = df["bedrooms"].min()
median_bdrms  = df["bedrooms"].median()
maximum_bdrms = df["bedrooms"].max()

print("minimum # of bedrooms:",minimum_bdrms) 
print("median  # of bedrooms:",median_bdrms) 
print("maximum # of bedrooms:",maximum_bdrms) 
print("")

print("median values:",df.median().values) 
print("")

prices = df["price"]
print("first 5 prices:")
print(prices.head()) 
print("")

median_price = df["price"].median()
print("median price:",median_price) 
print("")

corr_matrix = df.corr()
print("correlation matrix:")
print(corr_matrix["price"].sort_values(ascending=False))


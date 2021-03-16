import pandas as pd

df = pd.read_csv('multiple-delims2b.dat', 
                  names=['a', 'b', 'c', 'd'], 
                  sep=',', engine='python')

print("dataframe:")
print(df)


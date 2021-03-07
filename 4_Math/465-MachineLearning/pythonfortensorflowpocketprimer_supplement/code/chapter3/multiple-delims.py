import pandas as pd

df = pd.read_csv('multidelim.dat', skiprows=3, 
                  names=['a', 'b', 'c'], 
                  sep=' |:', engine='python')

print("dataframe:")
print(df)


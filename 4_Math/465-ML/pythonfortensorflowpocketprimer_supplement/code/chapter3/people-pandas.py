import pandas as pd

df = pd.read_csv('people.csv')
df.info()

print('fname:')
print(df['fname'])
print('------------')
print('age over 33:')
print(df['age'] > 33)
print('------------')
print('age over 33:')

myfilter = df['age'] >  33
print(df[myfilter])


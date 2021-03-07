import pandas as pd

df = pd.read_excel("employees.xlsx")
print("Contents of Excel spreadsheet:")
print(df)

print("Q1 sum, mean, min, max:")
print(df["q1"].sum(), df["q1"].mean(),df["q1"].min(),df["q1"].max())

print("Q2 sum, mean, min, max:")
print(df["q2"].sum(), df["q2"].mean(),df["q2"].min(),df["q2"].max())

print("Q3 sum, mean, min, max:")
print(df["q3"].sum(), df["q3"].mean(),df["q3"].min(),df["q3"].max())

print("Q4 sum, mean, min, max:")
print(df["q4"].sum(), df["q4"].mean(),df["q4"].min(),df["q4"].max())

sum_col=df[["q1","q2","q3","q4"]].sum()
print("Quarter totals:")
print(sum_col)


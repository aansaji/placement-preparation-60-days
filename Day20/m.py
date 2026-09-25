import pandas as pd

df = pd.read_csv("day20_messy_sales_data.csv")
print(df)
print(df.info())
print(df.isnull().sum())
print(df[df["Quantity"].isnull()])
print(df[df["Price"].isnull()])
df = df.dropna()
print(df.duplicated())
df = df.drop_duplicates()
print(df.duplicated().sum())
df["Product"] = df["Product"].str.lower()
df["Product"] = df["Product"].str.strip()
df["City"] = df["City"].str.title()
df["Payment"] = df["Payment"].str.upper()
print(df.dtypes)
df["Quantity"] = df["Quantity"].astype(int)
df["Revenue"] = df["Quantity"]*df["Price"]
print(df["Product"].value_counts())


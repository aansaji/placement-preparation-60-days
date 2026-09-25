import pandas as pd 
df = pd.read_csv("day19_sales_data.csv")
df["Date"] =pd.to_datetime(df["Date"])
df["Revenue"] = df["Quantity"]*df["Price"]
print(df)
daily_sales = df.groupby("Date")["Revenue"].sum()
print(daily_sales)
print(daily_sales.sort_values(ascending=False))
print(daily_sales.mean())

df["Day"] = df["Date"].dt.day_name()
print(df)
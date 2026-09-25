import pandas as pd

df = pd.DataFrame({
    "Name": ["Aan", "Rahul", "Anu", "Meera", "Arun"],
    "Marks": [85, 72, 95, 38, 67]
})

print(df)
print(df["Name"])
print(df[df["Marks"]>70])
print(df["Marks"].mean())
df["Passed"] = df["Marks"]>=40
print(df)
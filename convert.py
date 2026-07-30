import pandas as pd


# Read CSV
df = pd.read_csv("dataset/dataibm.csv")


# Convert CSV to JSON
df.to_json(
    "dataset/data.json",
    orient="records",
    indent=4
)


print("CSV converted to JSON successfully")
print("Rows converted:", len(df))
import os
import pandas as pd

path = os.getcwd() + "/data/"

csv_list = [pd.read_csv(path + f) for f in os.listdir(path)]
df = pd.concat(csv_list, ignore_index=True)
df.query("product == 'pink morsel'", inplace=True)

df["price"] = df["price"].apply(lambda x: float(x.strip("$")))
df["sales"] = (df["price"] * df["quantity"])
df = df.drop(columns=["product", "price", "quantity"])

df = df[["sales", "date", "region"]]
df.to_csv(path + 'pink_morsel_sales.csv', encoding='utf-8', index=False)




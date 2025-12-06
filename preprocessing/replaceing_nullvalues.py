import pandas as pd

df = pd.read_csv("/home/vijaylaxmi/stock_optimization_project/sales_data/sales_data(unprocessed).csv")
df['Opening_Stock'] = df['Opening_Stock'].fillna(1)

print(df)
import pandas as pd

#read csv file
df = pd.read_csv('/home/vijaylaxmi/stock_optimization_project/sales_data/sales_data.csv')

print("filtering products Whose Price is greater than 90:  ")
print()
high_price_items = df[df['Price'] > 90]

print(high_price_items[['Product_Name','Price','Units_Sold','Month']])

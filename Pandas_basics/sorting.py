import pandas as pd

#read csv file
df = pd.read_csv('/home/vijaylaxmi/stock_optimization_project/sales_data/sales_data.csv')


# Add Revenue column
df['Revenue'] = df['Units_Sold'] * df['Price']

print("HIGH PRICE TO LOW PRICE SORTING: ")
print()
sorted_price = df.sort_values(by='Price', ascending=False)          #sorting the products as high to low price
print(sorted_price[['Product_Name','Price','Units_Sold','Month']])

print("SORTING AS HIGH TO LOW SELLING PRODICTS: ")
print()
sorted_units = df.sort_values(by='Units_Sold', ascending=False)          #sorting to products as high selling to low selling
print(sorted_units[['Product_Name','Units_Sold','Price','Month']])


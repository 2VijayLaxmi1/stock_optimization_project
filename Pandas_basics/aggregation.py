import pandas as pd

#read csv file
df = pd.read_csv('/home/vijaylaxmi/stock_optimization_project/sales_data/sales_data.csv')
 

# Aggregation on Units_Sold
print("\nAggregation on Units_Sold:")
print(df['Units_Sold'].agg(['sum', 'mean', 'median', 'max', 'min']))

# Aggregation on Price
print("\nAggregation on Price:")
print(df['Price'].agg(['sum', 'mean', 'median', 'max', 'min']))

# Aggregation on Opening_Stock
print("\nAggregation on Opening_Stock:")
print(df['Opening_Stock'].agg(['sum', 'mean', 'median', 'max', 'min']))
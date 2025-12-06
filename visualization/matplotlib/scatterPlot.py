import pandas as pd
import matplotlib.pyplot as plt

#read csv file
df = pd.read_csv('/home/vijaylaxmi/stock_optimization_project/sales_data/sales_data.csv')

# Add Revenue column
df['Revenue'] = df['Units_Sold'] * df['Price']

plt.figure(figsize=(8,6))
plt.scatter(df['Units_Sold'], df['Revenue'], color='blue')

plt.title('Units Sold vs Revenue')
plt.xlabel('Units Sold')
plt.ylabel('Revenue')

plt.show()

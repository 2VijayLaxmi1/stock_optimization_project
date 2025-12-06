import pandas as pd
import matplotlib.pylab as plt

#read csv file
df = pd.read_csv('/home/vijaylaxmi/stock_optimization_project/sales_data/sales_data.csv')
 
#grouping by Product_Name and Units_sold for 6 months
product_sales = df.groupby("Product_Name")["Units_Sold"].sum()

#plot bar chart
plt.figure(figsize=(12,6))
plt.bar(product_sales.index,product_sales.values)

plt.title("Total Sales for each product in 6 months")
plt.xlabel("Product Name")
plt.ylabel("Total units sold")
plt.xticks(rotation=45)

plt.show()




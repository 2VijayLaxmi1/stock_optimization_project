import pandas as pd
import plotly.express as px

#read csv file
df = pd.read_csv('/home/vijaylaxmi/stock_optimization_project/sales_data/sales_data.csv')

#plot donut chart
fig= px.pie(
     df,
     names="Product_Name",
     values="Opening_Stock",
     title="opening stock for each product",
     hole=0.5

)
fig.show()
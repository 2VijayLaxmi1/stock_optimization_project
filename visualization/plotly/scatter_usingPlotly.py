import plotly.express as px
import pandas as pd

#read csv file
df = pd.read_csv('/home/vijaylaxmi/stock_optimization_project/sales_data/sales_data.csv')

#Scatter plot
fig=px.scatter(df,x="Opening_Stock",y="Units_Sold",
               color="Product_Name",title="Opening Stock VS Units Sold")
fig.show()
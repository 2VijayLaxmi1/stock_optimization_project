import pandas as pd
import plotly.express as px

#read csv file
df = pd.read_csv('/home/vijaylaxmi/stock_optimization_project/sales_data/sales_data.csv')
 
fig = px.histogram(df,x="Units_Sold",nbins=10, title=f"Distribution of Units Sold ")
fig.show()

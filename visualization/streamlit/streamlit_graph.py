import streamlit as st
import pandas as pd

# Read CSV file
df = pd.read_csv('/home/vijaylaxmi/stock_optimization_project/sales_data/sales_data.csv')

# Group by Product_Name and sum Units_Sold over 6 months
product_sales = df.groupby("Product_Name")["Units_Sold"].sum().reset_index()

# Streamlit title
st.title("Total Sales for Each Product in 6 Months")

# Plot line chart
# st.line_chart can take a DataFrame or Series directly
st.line_chart(data=product_sales.set_index('Product_Name'))

# Additional text
st.write("This is a line chart plotting total sales per product using Streamlit")

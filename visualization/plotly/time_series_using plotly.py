import pandas as pd
import plotly.express as px

#read csv file
df = pd.read_csv('/home/vijaylaxmi/stock_optimization_project/sales_data/sales_data.csv')

# Group by Month and sum Units_Sold
monthly_total = df.groupby("Month", as_index =False)["Units_Sold"].sum()
print(monthly_total)

# Correct month order
monthly_total["Month"] = pd.Categorical(
    monthly_total["Month"],
    categories=["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    ordered=True
    )

fig = px.line(
    monthly_total,
    x="Month",
    y="Units_Sold",
    title="Time Series of Total Units Sold per Month",
    markers=True
)

fig.show()
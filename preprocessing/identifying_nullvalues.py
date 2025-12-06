import pandas as pd
import matplotlib.pyplot as plt

#reasd csv file
df=pd.read_csv("/home/vijaylaxmi/stock_optimization_project/sales_data/sales_data(unprocessed).csv")

#print(df.head())

print(df.isnull().sum())
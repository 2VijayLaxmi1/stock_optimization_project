import pandas as pd

#read the csv file
df=pd.read_csv("/home/vijaylaxmi/stock_optimization_project/sales_data/sales_data(unprocessed).csv")

#drop all rows with any null value
'''df=df.dropna()
print(df)'''

#drop rows having null values in the specified column 
'''df=df.dropna(subset=['Price']))
print(df)'''

#Drop columns with any null value
#df=df.dropna(axis=1)


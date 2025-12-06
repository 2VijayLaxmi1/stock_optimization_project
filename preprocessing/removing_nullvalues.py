import pandas as pd

#read the csv file
df=pd.read_csv("/home/vijaylaxmi/stock_optimization_project/sales_data/sales_data(unprocessed).csv")

#drop row with null values
'''df=df.dropna()
print(df)'''

#drop the coloumn with null values
#df=df.drop(columns=['Product_ID'])


df=df.drop(columns=['Product_ID','Opening_Stock'])
print(df)
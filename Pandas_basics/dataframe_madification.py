import pandas as pd

#read csv file
df = pd.read_csv('/home/vijaylaxmi/stock_optimization_project/sales_data/sales_data.csv')

print(df.head())

####### Modifiying coloumns

df['Revenue'] = df['Units_Sold'] * df['Price']          #adding a new coloumn

df = df.drop(columns=['Opening_Stock'])                 #droping a coloumn 


''' we can drop coloum like this also: df = df.drop(['Opening_stock'])
                                                       df = df.drop(column=['Opening_stock'])
                                                       df = df.drop(column=['Opening_stock'],axis=1)
                                                        
                                                       THESE ALL WILL DO SAME THING 
                                                    
                        AND WE CAN ALSO DROP MULTIPLE COLOUMN BY ADDING COLOUMN NAME SEPARATED BY COMMAS
                                                    '''

df['Price'] = df['Price'] + 5                           #modify coloumn 
print(df)
print()

df = df.drop(index=1)                                   #droping a row based on index
print(df)

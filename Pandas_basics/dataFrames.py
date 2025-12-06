import pandas as pd

df=pd.DataFrame({'Item ':['Soap','chacolates','books','pens'],
                 'Quantity ':[50,10,50,30],
                 'Price':[55,15,45,5]}, index=['a','b','c','d'])

print(df)                   #print the full df
print()

print(df.head())            #print first 5 rows 
print()

print(df.tail())            #print last 5 rows
print()


print(df.head(2))           #print first 2 rows
print()

print(df.tail(2))           #print last 2 rows
print()

print(df.shape)             #print (rows,coloumns)
print()

print(df.columns)          #prints name and datatype of all coloumns
print()

print(df.iloc[3])           #print row based on position index
print()


print(df.loc['a'])         #print row based on customized index


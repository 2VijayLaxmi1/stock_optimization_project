import pandas as pd
data=pd.Series([10,20,30,40,50])
for i in data:
    print(i)                        # this will the series element

print()

print(data)
print()

# this will print data_2 with customized index
data_2= pd.Series(["Priya", "Rahul", "Anjali", "Vikram", "Sunita", "Amit"],index=[10,11,12,13,14,15])
print(data_2)                       
print()

# print series using range
data_3= pd.Series(["Priya", "Rahul", "Anjali", "Vikram", "Sunita", "Amit"],index=[i for i in range(5,11)])
print(data_3)


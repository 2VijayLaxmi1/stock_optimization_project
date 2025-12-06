import numpy as np
################################creating array

arr_1 = np.array([1,2,3,4,5,6])                    #created 1D array 

arr_2 = np.array([[1,2,3,4,5],                      #created 2D array
                 [6,7,8,9,10]])

arr_3 = np.zeros(5)                                 #created 1D zero array of size 5

arr_4 = np.zeros((2,5))                             #created 2D zero array of 2 row and 5 coloumns

arr_5 = np.ones((2,5))                              #created 2D ones array of 2 row and 5 coloumns

arr_6 = np.arange(0,6)                              #created array using arange

print( arr_1 , '\n\n', arr_2 ,'\n\n',arr_3 ,'\n\n',arr_4 ,'\n\n',arr_5 ,'\n\n',arr_6)
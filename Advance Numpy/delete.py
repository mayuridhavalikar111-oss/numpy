''' 
removes the specific element from the array on the basis of index and returns a new array without that element.
'''

import numpy as np

arr=np.array([10,20,30,40,50])
print(arr)

new_arr=np.delete(arr,2)  #it will remove the element at index 2
print(new_arr)


#deleting a row from 2d array
arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
new_2d_arr=np.delete(arr_2d, 0, axis=0)  #it will remove the row at index 0   
print(new_2d_arr)
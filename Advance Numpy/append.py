'''Adding element at the end of an array
New array will get created original array will remain same
'''
import numpy as np

arr=np.array([10,20,30,40])
print(arr)

new_arr=np.append(arr, [50,60,70,80])
print("New array after appending is:", new_arr)

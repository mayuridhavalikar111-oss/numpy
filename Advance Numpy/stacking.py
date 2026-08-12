'''
vstack()- row wise stacking
hstack()-cloumn wise stacking
'''
import numpy as np

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print("Array1=",arr1)
print("Array2=",arr2)

print("Row wise stacking")
print(np.vstack((arr1,arr2))) #Vertical stacking

print("Column wise stacking")
print(np.hstack((arr1,arr2))) #Horizontal stacking


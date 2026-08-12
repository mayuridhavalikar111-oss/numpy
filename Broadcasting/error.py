import numpy as np

arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([1,2])

result=arr1+arr2
print(result)

'''it shows shape error because arr1 is 2D array and arr2 is 1D array. so we can not add them directly.'''

#Solution: we can use broadcasting to add them. we can reshape arr2 to make it 2D array.
arr2=arr2.reshape(2,1)
result=arr1+arr2    
print(result)

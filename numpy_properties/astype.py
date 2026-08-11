#Converting data types of array elements using astype() function
#Used for changing data types
import numpy as np
arr=np.array([1.2,3.4,7.7])
print(arr)
print(arr.dtype)

#After converting array to integer:
int_arr=arr.astype(int)
print(int_arr)
print(int_arr.dtype)

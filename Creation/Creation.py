#Creating arrays from python lists

import numpy as np
arr=np.array([1,2,3,4])
print(arr)


#with default values:
#np.zeros(shape) (3) fir 1d, (3,3) 2d

zeros_array=np.zeros(3)
print(zeros_array)

#ones(shape)
ones_array=np.ones((2,3))
print(ones_array)

#Full Function
filled_array=np.full((2,2),7)
print(filled_array)


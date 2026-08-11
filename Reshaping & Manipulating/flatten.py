''' ravel()-- it returns views
flatten()-- it returns copy'''

'''flatten() is used when their is need to convert multi-dimensional array into one dimensional array'''


import numpy as np
arr_2d=np.array([[1,2,3],[4,5,6]])
print(arr_2d.ravel())
print(arr_2d.flatten())

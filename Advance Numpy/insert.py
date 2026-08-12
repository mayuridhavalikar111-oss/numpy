'''
np.insert(array,index,value,asix=none)
'''

import numpy as np
arr=np.array([10,20,30,40,50])
print(arr)
new_arr=np.insert(arr,2,100)  #it will make changes at index 2 and insert 100
print(new_arr)

import numpy as np
#ndarray.ndim  It returns the number of array dimentions


# 1-D array

x = np.array([1, 2, 3])
x.ndim

# 2-D array

Y = np.array([[1, 2, 3], [4,5,6], [7,8,9], [10,11,12]])
Y.ndim

#The tuple (2, 3, 4(passed as an argument represents the shape of the ndarray

y = np.zeros((2,3,4))
y.ndim

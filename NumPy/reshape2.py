import numpy as np

#Create a Numpy array by calling the reshape() function from the output of arange() function

Y = np.arange(20).reshape(4,5)

print()
print('Y = \n', Y)
print()

print('Y has dimensions:', Y.shape)
print('Y is an object of type:', type(Y))
print('The elements in Y are of type:', Y.dtype)


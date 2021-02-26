import numpy as np

# Create a Numpy array by feeding the output of arange() function as an argument to the reshape() function.

x = np.arange(20)

print()
print('Original x = ', x)
print()

x = np.reshape(x, (4,5))

print()
print('Reshaped x = \n', x)
print()

print('x hax dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)

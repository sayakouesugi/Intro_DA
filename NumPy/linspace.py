import numpy as np

#linspace(start, stop, n)

# We create a rank 1 ndarray that has 10 integers evenly spaced between 0 and 25.

x = np.linspace(0,25,10)

print()
print('x = \n', x)
print()

print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)



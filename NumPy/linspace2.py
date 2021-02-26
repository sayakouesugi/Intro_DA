import numpy as np

#Create a Numpy array using linspace(start, stop, n) with stop excluded

#We create a rank 1 ndarray that has 10 integers evenly spaced between 0 and 25
#with 25 excluded 

x = np.linspace(0,25,10, endpoint = False)

print()
print('x = ', x)
print()

print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)

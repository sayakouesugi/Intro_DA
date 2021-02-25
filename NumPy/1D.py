import numpy as np

x = np.array([1,2,3,4,5])

print('x = ', x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)


"""Output should be 
   x has dimensions:(5,)
   x is an object of type: class 'numpy.ndarray'
   The elements in x are of type: int 64
   """

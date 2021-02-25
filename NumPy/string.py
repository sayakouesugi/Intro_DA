import numpy as np

x = np.array(['Hello', 'World'])

print('x = ', x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)

""" 
The output should be 

x has dimensions:(2,)
x is an object of type: class 'numpy.ndarray'
the elements in x are of type: U5
"""

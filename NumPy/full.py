import numpy as np

# We create a 2 x 3 ndarray full of fives

X = np.full((2,3), 5)

print()
print('X = \n', X)
print()

print('X has dimensions: ', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of types:', X.dtype)

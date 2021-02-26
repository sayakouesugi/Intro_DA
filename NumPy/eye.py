import numpy as np

# We create a 5 x 5 Identity matrix

X = np.eye(5)

print()
print('X = \n', X)
print()

print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are:', X.dtype)

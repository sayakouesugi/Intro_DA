import numpy as np

# Modify an element of 2-D array

X = np.array([[1,2,3],[4,5,6],[7,8,9]])

print()
print('Original:\n X = \n', X)
print()

X[0,0] = 20

print('Modified:\n X = \n', X)

""" Original 
  X = 
  [[1 2 3]
   [4 5 6]
   [7 8 9]]

   Modified 
   X =
   [[20 2 3]
    [4 5 6]
    [7 8 9]]
    """

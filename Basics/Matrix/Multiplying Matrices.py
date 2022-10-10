# Multiply given matrices of any order

import numpy as np


def mulMat(mat1, mat2):
    return np.dot(mat1, mat2)


# Driver code
X = [[1, 7, 3], [3, 5, 6], [6, 8, 9]]
Y = [[1, 1, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]

for i in mulMat(X, Y):
    print(i)

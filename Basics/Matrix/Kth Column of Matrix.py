# Get the column at Kth index in a given multi-dimensional matrix


def getCol(mat, k):
    return list(zip(*mat))[k]


# Driver code
mat = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]
print(getCol(mat, 1))

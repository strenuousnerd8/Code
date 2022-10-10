# Add two matrices of order N


def addMat(mat1, mat2):
    res = []
    for i in range(len(mat1)):
        res.append([])
        for j in range(len(mat1[i])):
            res[i].append(mat1[i][j] + mat2[i][j])
    return res


# Driver code
X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

for i in addMat(X, Y):
    print(i)

R, C = int(input("Rows:\t")), int(input("Columns:\t"))
mat = [[int(input()) for i in range(C)] for j in range(R)]
for row in mat:
    print(row)

# import numpy
# R = int(input("Rows:\t"))
# C = int(input("Columns:\t"))
# mat = []
# for i in range(R*C):
#     mat.append(int(input()))
# print(numpy.array(mat).reshape(R, C))
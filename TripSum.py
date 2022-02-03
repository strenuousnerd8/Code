#Code a program that outputs permutations of three given inputs in lists whose sum is not more than provided N
x, y, z, N = int(input("X: ")), int(input("Y: ")), int(input("Z: ")), int(input("N: "))
print([[i,j,k] for i in range(x) for j in range(y) for k in range(z) if i+j+k<=N])

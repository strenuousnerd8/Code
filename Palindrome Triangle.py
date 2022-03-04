n = int(input())
spaces = range(n)[::-1]
for i in range(1, n + 1):
	print(" "*spaces[i-1] + str((111111111//(10**(9-i)))**2))
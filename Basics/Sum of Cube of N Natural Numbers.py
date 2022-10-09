# Find the sum of cube of all N natural numbers

n = int(input())
print(sum(i**3 for i in range(1, n + 1)))

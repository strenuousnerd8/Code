n = int(input())
for i in range(n, 0, -1):
    print(" " * i, ['* ' * i for i in range(1, n + 1)][::-1][i - 1])
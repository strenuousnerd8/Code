# Triangle Pattern using Asterisk / Star
n = int(input())
for i in range(n, 0, -1):
    print(" " * i, ['* ' * i for i in range(1, n + 1)][::-1][i - 1])

# Integers pattern with each line starting from 1
n = int(input())
for i in range(n, 0, -1):
    print(" " * i, *[list(range(1, i + 1)) for i in range(1, n + 1)][::-1][i - 1], sep=" ")

# Diamond Pattern using Asterisk / Star
n = int(input())
for i in range(n, 0, -1):
    print(" " * i, ['* ' * i for i in range(1, n + 1)][::-1][i - 1])
for i in range(1, n):
    print(" " * (i + 1), ['* ' * i for i in range(1, n)][::-1][i - 1])

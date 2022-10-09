# Fibonacci sequence
def fibonacciSeq(n):
    a, b = 0, 1
    res = [a, b]
    for _ in range(2, n):
        c = a + b
        res.append(c)
        a, b = b, c
    return res


# Driver code
print(*fibonacciSeq(int(input())), sep=" ")

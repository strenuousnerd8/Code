# Find factorial of a given number

# Recursive method
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


# Iterative method
def factorial(n):
    if n == 1:
        return 1
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


# Driver code
print(fact(int(input())))

print(factorial(int(input())))

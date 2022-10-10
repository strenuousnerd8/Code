# Find the Highest Common Factor of two numbers in python


# Using Euclidean Algo
import math


def findHCF(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


# Using Math module
print(math.gcd(60, 12))

# Driver code
print(findHCF(60, 48))

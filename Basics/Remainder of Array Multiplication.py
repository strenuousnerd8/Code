# Multiply all the numbers in the array and find the remainder after dividing with n


# Using distributive law of modular arithmetic to avoid 2 ^ 64 int size overflow
# ( a * b ) % c = ( ( a % c ) * ( b % c ) ) % c


def finder(arr, n):
    mul = 1
    for i in arr:
        mul = mul * (i % n)
    return mul % n


# Driver code
arr = [100, 10, 5, 25, 35, 14]
n = 11
print(finder(arr, n))

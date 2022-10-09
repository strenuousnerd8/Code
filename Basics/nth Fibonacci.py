# Find the nth fibonacci number


from math import sqrt

n = 8
res = (((1 + sqrt(5)) ** n) - ((1 - sqrt(5))) ** n) / (2**n * sqrt(5))
print(int(res))

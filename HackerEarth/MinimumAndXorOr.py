# Condition: Minimum (a[i] and a[j]) xor (a[i] or a[j])
from itertools import permutations
t = int(input())
while t != 0:
    n = int(input())
    perm = list(permutations(list(map(int, input().split())), 2))
    print(min([(i[0] and i[1]) ^ (i[0] or i[1]) for i in perm]))
    t-=1
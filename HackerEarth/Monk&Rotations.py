# Rotate an integer string to the right k number of time
t  = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    x = k%n
    print(*(l[n-x:]+l[:n-x]))
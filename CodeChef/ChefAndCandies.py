# cook your dish here
t = int(input())
while t != 0:
    n, x = map(int, input().split())
    if x < n:
        count = 0
        remain = n - x
        while remain > 0:
            remain -= 4
            count += 1
        print(count)
    else:
        print(0)
    t-=1
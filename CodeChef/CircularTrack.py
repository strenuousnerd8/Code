for _ in range(int(input())):
    a, b, m = map(int, input().split())
    a,b = min(a,b),max(a,b)
    print(min(b-a,m-b+a))
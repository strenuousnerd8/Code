t = int(input())
while t != 0:
    n, height = map(int, input().split())
    heights = list(map(int, input().split()))
    print(len([i for i in heights if i > height]))
    t -= 1
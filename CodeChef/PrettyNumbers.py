t = int(input())
while t != 0:
    here, there = map(int, input().split())
    print(len([i for i in range(here, there + 1) if str(i)[-1] == '2' or str(i)[-1] == '3' or str(i)[-1] == '9']))
    t -= 1
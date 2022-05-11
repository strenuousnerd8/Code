t = int(input())
while t != 0:
    digital = {
        0: 6, 1: 2, 2: 5,
        3: 5, 4: 4, 5: 5,
        6: 6, 7: 3, 8: 7,
        9: 6
    }
    res = sum(map(int, input().split()))
    total = 0
    for i in str(res):
        total += digital[int(i)]
    print(total)
    t -= 1
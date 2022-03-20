# Condition: Minimum (a[i] and a[j]) xor (a[i] or a[j])
t = int(input())
while t != 0:
    n = int(input())
    perm, res = sorted(list(map(int, input().split())), reverse=True), []
    for i, data in enumerate(perm):
        try:
            res.append(perm[i+1] ^ data)
        except IndexError:
            pass
    print(min(res))
    t-=1
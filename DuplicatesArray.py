arr = [2, 3, 4, 4, 5, 6, 6, 6, 8, 8]
res = []
for i in range(len(arr) - 1):
    if arr[i] != arr[i + 1]:
        res.append(arr[i])
res.append(arr[-1])
print(res)
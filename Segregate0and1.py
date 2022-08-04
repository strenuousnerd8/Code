# Separate the 0s and 1s in the from binary array
arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
n = len(arr)
count = 0
res = []
for i in range(n):
    if arr[i] == 0:
        count += 1
for i in range(n):
    if i <= (count - 1):
        res.append(0)
    else:
        res.append(1)
print(res)
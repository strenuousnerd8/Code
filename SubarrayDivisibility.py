array = [3, 1, 2, 5, 1]
n = 3
res = []
for i in range(0, len(array)+1):
    for j in range(0, len(array)+1):
        if array[i:j] != [] and sum(array[i:j]) % n == 0:
            res.append(array[i:j])
print(len(res))
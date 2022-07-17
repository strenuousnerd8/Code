# Sort only the even elements of the array without changing the order of the odd elements
arr = [4, 7, 2, 11, 15]
evens = sorted([i for i in arr if i % 2 == 0])
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        arr[i] = evens[0]
        evens.pop(0)
print(arr)
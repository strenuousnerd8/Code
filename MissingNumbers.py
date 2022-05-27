def missing(arr):
    return sorted(set(range(arr[0], arr[-1])) - set(arr))

arr = [1, 2, 4, 6, 7, 9, 10]
print(missing(arr))
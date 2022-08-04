# Find the two missing numbers in the sequential series
def get(arr, n):
    res = []
    mark = [False for i in range(n + 1)]
    for i in range(n - 2):
        mark[arr[i]] = True
    for i in range(1, n + 1):
        if not mark[i]:
            res.append(i)
    return res

# Driver Code
arr = [1, 2, 4, 6, 7]
print(get(arr, len(arr) + 2))
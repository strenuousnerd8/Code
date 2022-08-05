# Find the missing number in the given Arithmetic Progression
def bsearch(arr, low, high, diff):
    while low <= high:
        mid = (low + high) // 2
        if (arr[mid] - arr[0]) // diff == mid:
            low = mid + 1
        else:
            high = mid - 1
    return arr[high] + diff

def get(arr, n):
    diff = (arr[-1] - arr[0]) // n
    return bsearch(arr, 0, n - 1, diff)

arr = [3, 9, 12, 15]
n = len(arr)
print(get(arr, n))
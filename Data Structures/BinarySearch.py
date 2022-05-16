def BinarySearch(arr, n, low, high, data):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if arr[mid] == data:
            return mid
        elif arr[mid] < data:
            return BinarySearch(arr, n, mid + 1, high, data)
        else:
            return BinarySearch(arr, n, low, mid - 1, data)


arr = [5, 9, 17, 23, 25, 45, 59, 63, 71, 89]
n = 10
data = 59
print(BinarySearch(arr, n, 0, n-1, data))
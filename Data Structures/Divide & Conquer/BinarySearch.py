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
        # (or just) return mid if arr[mid] == data else BinarySearch(arr, n, mid + 1, high, data) if arr[mid] < data else BinarySearch(arr, n, low, mid - 1, data)


arr = [20, 21, 39, 43, 49, 54, 73, 85, 96]
n = 9
data = 96
print(BinarySearch(arr, n, 0, n-1, data))
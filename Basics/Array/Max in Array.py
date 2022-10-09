# Find the max value in an array


def findMax(arr):
    curr = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > curr:
            curr = arr[i]
    return curr


# Driver code
arr = [2, 6, 2, 7, 1]
print(findMax(arr))

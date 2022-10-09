# Rotate an array by n steps using list slicing


def rotateArr(arr, n):
    return arr[n:] + arr[:n]


# Driver code
arr = [1, 2, 3, 4, 5, 6, 7]
steps = 4
print(rotateArr(arr, steps))

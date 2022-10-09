# Find if an array is monotone (if it is same in ascending and descending order to original array after sorting)


def monotone(arr):
    res = sorted(arr)
    if res == arr or res[::-1] == arr:
        return True
    return False


# Driver code
arr = [6, 5, 4, 4]
print(monotone(arr))

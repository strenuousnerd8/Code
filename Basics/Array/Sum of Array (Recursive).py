# Recursively find the sum of all elements in the given array


def findSum(arr, sum=0):
    if not arr:
        return sum
    sum += arr.pop()
    return findSum(arr, sum)


# Driver code
arr = [1, 2, 3, 4]
print(findSum(arr))

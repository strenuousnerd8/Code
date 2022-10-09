# Find the cumulative sum of all elements in the array


def findCumu(arr):
    for i in range(1, len(arr) + 1):
        print(sum(arr[:i]), end=" ")


# Driver code
arr = [10, 20, 30, 40, 50]
findCumu(arr)

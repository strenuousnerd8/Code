# Sort the given array array using positions in auxiliaxy array provided


# Using zip() for zipping 2 lists together
def sortArr(a, b):
    c = zip(b, a)
    print(*[x for _, x in sorted(c)], sep=" ")


# Driver code
arr1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
arr2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]
sortArr(arr1, arr2)

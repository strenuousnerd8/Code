def BubbleSort(arr, n):
    changed = True
    while changed:
        changed = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                changed = True
    return arr

arr = [20, 21, 39, 43, 49, 54, 73, 85, 96]
n = 9
print(BubbleSort(arr, n))
def BubbleSort(arr, n):
    changed = True
    while changed:
        changed = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                changed = True
    return arr

arr = [6, 1, 6, 7, 8, 5, 8, 9, 1]
n = 9
print(BubbleSort(arr, n))
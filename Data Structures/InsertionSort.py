def insertion_sort(arr):
    for i, value in enumerate(arr):
        for j in range(i - 1, -1, -1):
            if arr[j] > value:
                arr[j + 1] = arr[j]
                arr[j] = value
    return arr
if __name__ == '__main__':
    print(insertion_sort([4, 2, 6, 5, 1, 3]))
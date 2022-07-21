#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
from copy import *

def almostSorted(n, arr):
    # Write your code here
    sortarr = sorted(arr)
    if sortarr == arr:
        return "yes"

    l = r = 0
    for i in range(n - 1):
        if arr[i + 1] < arr[i]:
            l = i
            break
    for j in range(n - 1, 0, -1):
        if arr[j - 1] > arr[j]:
            r = j
            break

    temp = deepcopy(arr)
    temp[l], temp[r] = temp[r], temp[l]
    if temp == sortarr:
        temp = True

    if temp is not True:
        temp = arr[:l] + arr[l : r + 1][::-1] + arr[r + 1:]
        if temp == sortarr:
            print("yes")
            print('reverse {} {}'.format(l + 1, r + 1))
        else:
            print("no")
    else:
        print("yes")
        print('swap {} {}'.format(l + 1, r + 1))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().split()))

    almostSorted(n, arr)

# Find the subarrays with target sum within a given array using sliding window
# Time: O(n ^ 2), Space: O(1)
def findSum(arr, target):
    subs = []
    l, r = 0, 1
    while r < len(arr):
        if sum(arr[l : r + 1]) == target:
            subs.append(arr[l : r + 1])
            r += 1
        elif sum(arr[l : r + 1]) < target:
            r += 1
        else:
            l += 1
    return subs


arr = [2, 6, 0, 9, 7, 3, 1, 4, 1, 10]
target = 15
print(findSum(arr, target))
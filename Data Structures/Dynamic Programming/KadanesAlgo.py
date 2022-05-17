# Find the maximum subarray sum within a given array using Kadane's Algorithm
# Time: O(n), Space: O(1)
def Kadane(arr):
    max_current = max_global = arr[0]
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current
    return max_global

arr = [1,2,3,-2,5]
print(Kadane(arr))
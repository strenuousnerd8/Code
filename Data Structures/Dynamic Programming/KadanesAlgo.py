# Find the maximum subarray sum within a given array using Kadane's Algorithm
# Time: O(n), Space: O(1)
def Kadane(arr):
    max_current = max_global = arr[0]
    left_index = r_index = 0
    for i in range(1, len(arr)):
    # Fast solution

    #     max_current = max(arr[i], max_current + arr[i])
    #     if max_current > max_global:
    #         max_global = max_current
    # return max_global

    # Returning Indexes
        if arr[i] > max_current + arr[i]:
            left_index = i
            max_current = arr[i]
        else:
            max_current = arr[i] + max_current

        if max_current > max_global:
            max_global = max_current
            r_index = i 

    return left_index, r_index, arr[left_index: r_index], max_global



arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(Kadane(arr))
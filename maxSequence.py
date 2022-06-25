def maxSubArray(n, arr):
    my_dict = dict()
    for i in range(n):
        my_dict[i] = []
        my_dict[i].append(splitter(arr[i:]))
    for i in my_dict:
        my_dict[i] = sum([sum(i) for i in my_dict[i][0]])
    maxim = max(my_dict.values())
    return maxim

def splitter(arr):
    res = []
    count = 1
    i = 0
    while count < len(arr) - i + 1:
        res.append(arr[i: count + i])
        i += count
        count += 1
    return res

n = 3
arr = [2, 1, 3, 9, 2, 4, -10, -9, 1, 3]
print(maxSubArray(n, arr))
def topKFrequent(nums, k):
    my_dict = dict()
    hmap = [[] for _ in range(1, len(nums) + 1)]
    for _ in nums:
        my_dict[_] = 1 + my_dict.get(_, 0)
    for key, val in my_dict.items():
        hmap[val].append(key)

    res = []
    for i in range(len(hmap) - 1, 0, -1):
        for j in hmap[i]:
            res.append(j)
            if len(res) == k:
                return res

print(topKFrequent([1, 3, 2, 1, 4, 1], 2))
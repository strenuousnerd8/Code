def topKFrequent(nums, k):
    numDict = {}
    for num in nums:
        if num not in numDict:
            numDict[num] = 1
        else:
            numDict[num]+= 1
    return((sorted(numDict, key = numDict.get, reverse=True))[0:k])

print(topKFrequent([1, 3, 2, 1, 4, 1], 2))
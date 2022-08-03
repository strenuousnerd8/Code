class Solution:
    def medianSlidingWindow(nums, k):
        res = []
        for i in range((len(nums) - k) + 1):
            current = sorted(nums[i : i + k])
            if len(current) % 2 != 0:
                res.append(round(float(current[len(current) // 2]), 5))
            else:
                res.append(round(float((current[(len(current) // 2) - 1] + current[(len(current) // 2)]) / 2), 5))
        return res


print(Solution.medianSlidingWindow([1,2,3,4,2,3,1,4,2], 3))
# print(Solution.medianSlidingWindow(list(map(int, input().split())), int(input())))
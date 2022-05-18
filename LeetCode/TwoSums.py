# Twosum :) ifkyk
class Solution:
    def twoSum(self, nums, target):
        complementMap = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if nums[i] in complementMap:
                return [complementMap[nums[i]], i]
            else:
                complementMap[complement] = i

Answer = Solution()
print(Answer.twoSum([2,7,11,15], 26))
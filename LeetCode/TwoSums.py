# Twosum :) ifkyk
class Solution:
    def twoSum(self, nums, target):
        prev = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prev:
                return [prev[diff], i]
            prev[nums[i]] = i

Answer = Solution()
print(Answer.twoSum([2,7,11,15], 26))
# Twosum :) ifkyk
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i,j]

Answer = Solution()
print(Answer.twoSum([2,7,11,15], 26))
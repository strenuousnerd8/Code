class Solution:
    def twoSum(self, nums, target):
        prev = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prev:
                return [prev[diff], i]
            prev[nums[i]] = i

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
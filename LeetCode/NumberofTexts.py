class Solution:
    def countTexts(self, keys: str) -> int:
        dp = [1]
        prev = None
        for key in keys:
            keep = 1 if key != prev else 3 + (key in '79')
            del dp[:-keep]
            dp.append(sum(dp) % 1000000007)
            prev = key
        return dp[-1]

new = Solution()
print(new.countTexts("22233"))
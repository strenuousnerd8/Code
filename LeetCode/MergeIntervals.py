class Solution:
    def merge(self, intervals):
        res = []
        intervals.sort()
        for interval in intervals:
            if not res:
                res.append(interval)
            else:
                if res[-1][1] < interval[0]:
                    res.append(interval)
                else:
                    res[-1][1] = max(interval[1], res[-1][1])
        return res

new = Solution()
print(new.merge([[1,3],[2,6],[8,10],[15,18]]))
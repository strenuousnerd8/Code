class Solution:
    def maxProfit(self, prices):
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                currentProfit = prices[right] - prices[left]
                if currentProfit > max_profit:
                    max_profit = currentProfit
            else:
                left = right
            right += 1
        return max_profit
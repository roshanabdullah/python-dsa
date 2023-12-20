# Top-down approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = 0

        for sell in prices[1:]:
            if sell > buy:
                maxProfit = max(maxProfit, sell - buy)
            else:
                buy = sell
        return maxProfit

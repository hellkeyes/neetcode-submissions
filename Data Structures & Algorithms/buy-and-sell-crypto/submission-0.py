class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_sell = prices[0]
        max_profit = 0
        i = 1

        while i < len(prices):
            if prices[i] < min_sell:
                min_sell = prices[i]

            profit = prices[i] - min_sell

            max_profit = max(max_profit, profit)

            i += 1

        return max_profit
 

        
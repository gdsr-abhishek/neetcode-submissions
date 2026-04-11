class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit  =  0
        days = len(prices)
        last_day = days
        for i in range(days):
            current_day = i + 1
            while current_day < last_day:
                estimated_profit = prices[current_day] - prices[i]
                if estimated_profit > 0:
                    max_profit = max(max_profit,estimated_profit)
                current_day +=1
        return max_profit 
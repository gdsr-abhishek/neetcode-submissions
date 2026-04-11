class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]    # cheapest buy so far (left side of window)
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)           # track lowest buy point
            max_profit = max(max_profit, price - min_price)  # best sell today?

        return max_profit
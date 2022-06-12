class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        len_prices = len(prices)
        max_profit = 0
        max_price = prices[-1]
        for i in range(len_prices-2,-1,-1):
            if prices[i]>max_price: 
                max_price = prices[i]
            current_profit = max_price-prices[i]
            max_profit = max(current_profit, max_profit)
        return max_profit

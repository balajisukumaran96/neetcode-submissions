class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        if n==0 or n == 1:
            return 0

        left = 0
        right = 0
        max_profit = float("-inf")

        while right < n:
            while left < right and prices[left] > prices[right]:
                left += 1
            
            current_profit = prices[right] - prices[left]
            max_profit = max(max_profit, current_profit)     
            right += 1

        return max_profit

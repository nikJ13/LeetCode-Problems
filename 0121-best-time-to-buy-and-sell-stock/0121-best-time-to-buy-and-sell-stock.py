class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        temp_buy = float("inf")
        for p in prices:
            if p<temp_buy:
                temp_buy = p
            else:
                max_profit = max(max_profit, p - temp_buy)
        return max_profit
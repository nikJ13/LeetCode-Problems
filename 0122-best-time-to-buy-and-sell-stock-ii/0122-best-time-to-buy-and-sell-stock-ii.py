class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = float("inf")
        ans = 0
        for i in range(len(prices)):
            if prices[i]<curr_min:
                curr_min = prices[i]
            else:
                profit = prices[i] - curr_min
                ans += profit
                curr_min = prices[i]
        return ans
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        iterate through the array and
        if curr_max>curr_element:
            calculate the profit
            check if this is the maximum profit
        else:
            curr_max = curr_element
        """
        curr_min = float("inf")
        ans = 0
        for i in range(len(prices)):
            if curr_min<prices[i]:
                profit = prices[i] - curr_min
                ans = max(ans,profit)
            else:
                curr_min = prices[i]
        return ans
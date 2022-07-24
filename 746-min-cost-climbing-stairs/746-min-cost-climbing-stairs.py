class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans = 1000
        dp = [-1]*len(cost)
        def recurse(index):
            if index>=len(cost):
                return 0
            if dp[index]!=-1:
                return dp[index]
            dp[index] = cost[index] + min(recurse(index+1),recurse(index+2))
            return dp[index]
        return min(recurse(0),recurse(1))
        
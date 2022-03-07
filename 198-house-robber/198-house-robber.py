class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for _ in range(n)]
        ans = 0
        def recurse(index):
            if index==n-2 or index==n-1:
                dp[index] = nums[index]
                return dp[index]
            if dp[index]!=-1:
                return dp[index]
            for i in range(index+2,n):
                res = recurse(i)
                dp[index] = max(nums[index]+res,dp[index])
            return dp[index]
        #print(dp)
        for j in range(n):
            if dp[j]==-1:
                tmp = recurse(j)
                ans = max(tmp,ans)
        return ans
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)
        n = len(nums)
        dp = [[0 for _ in range(n)] for t in range(3)]
        max1 = -1
        for i in range(3):
            for j in range(i,n):
                if i==0 and j==n-1:
                    dp[i][j] = dp[i][j-1]
                    continue
                if j-i==2:
                    dp[i][j] = nums[i] + nums[j]
                elif j-i>2:
                    dp[i][j] = nums[j] + max(dp[i][j-2],dp[i][j-3])
                else:
                    dp[i][j] = nums[i]
                if j>=n-3:
                    max1 = max(max1,dp[i][j])
        print(dp)
        return max1
        
        
                
                
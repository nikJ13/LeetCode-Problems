class Solution {
    int[] dp;
    public int helper(int[] dp, int n){
        if(dp[n]!=-1){
            return dp[n];
        }
        dp[n] = helper(dp,n-1) + helper(dp,n-2);
        return dp[n];
    }
    public int climbStairs(int n) {
        dp = new int[n+1];
        for(int i=0;i<n+1;i++){
            if(i==1){
                dp[i] = 1;
            }else if (i==2){
                dp[i] = 2;
            }else{
                dp[i] = -1;
            }
        }
        return helper(dp,n);
        
    }
}
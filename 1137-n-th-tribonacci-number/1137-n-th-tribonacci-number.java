class Solution {
    int[] dp; // global memoization array; this initially means that 'dp' is null
    public int helper(int n,int[] dp){
        if(dp[n]!=-1){
            return dp[n];
        }
        dp[n] = helper(n-1,dp)+helper(n-2,dp)+helper(n-3,dp);
        return dp[n];
    }
    public int tribonacci(int n) {
        dp = new int[n+1]; // 'dp' is defined as an array here, with size of 'n+1'
        for(int i=0;i<n+1;i++){
            if(i==0){
                dp[i] = 0;
            }else if(i==1 || i==2){
                dp[i] = 1;
            }else{
                dp[i] = -1;
            }
        }
        return helper(n,dp);
    }
}
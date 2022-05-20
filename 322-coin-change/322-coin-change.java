class Solution {
    public int coinChange(int[] coins, int amount) {
        if(amount==0){
            return 0;
        }
        int[] dp = new int[amount+1];
        for(int i=1;i<dp.length;i++){
            dp[i] = amount+1;
        }
        for(int i=0;i<coins.length;i++){
             for(int j=0;j<amount+1;j++){
                 if(coins[i]==j){
                     dp[j] = 1;
                 }else if(coins[i]<j){
                     dp[j] = Math.min(dp[j-coins[i]] + 1,dp[j]);
                 }
             }
        }
        if(dp[amount]==amount+1){
            return -1;
        }
        return dp[amount];
    }
}
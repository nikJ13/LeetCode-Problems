class Solution {
    int[] dp;
    public int helper(int[] dp, int[] cost, int index){
        if(index>=dp.length){
            return 0;
        }
        if(dp[index]!=-1){
            return dp[index];
        }
        dp[index] = cost[index] + Math.min(helper(dp,cost,index+1),helper(dp,cost,index+2));
        return dp[index];
    }
    public int minCostClimbingStairs(int[] cost) {
        dp = new int[cost.length];
        for(int i=0;i<cost.length;i++){
            dp[i] = -1; 
        }
        return Math.min(helper(dp,cost,0),helper(dp,cost,1));
    }
}
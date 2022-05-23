class Solution {
    public int integerBreak(int n) {
        int[] dp = new int[n+1];
        dp[1] = 1;
        for(int i=2;i<n+1;i++){
            int max = Integer.MIN_VALUE;
            for(int j=1;j<=i/2;j++){
                int product = Math.max(dp[j],j)*Math.max(dp[i-j],i-j);
                max = Math.max(max,product);
            }
            dp[i] = max;
        }
        return dp[n];
    }
}
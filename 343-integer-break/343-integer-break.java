class Solution {
    public int integerBreak(int n) {
        int[] dp = new int[n+1];
        dp[1] = 1;
        for(int i=2;i<n+1;i++){
            int max = Integer.MIN_VALUE;
            for(int j=1;j<=i/2;j++){ // we iterate till i by two because the numbers beyond that half will give the same product value
                int product = Math.max(dp[j],j)*Math.max(dp[i-j],i-j); // here, for each number, we check if we can get either the max product by considering then current number itself or the max product for the current number
                max = Math.max(max,product);
            }
            dp[i] = max;
        }
        return dp[n];
    }
}
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        // here we count the length of the largest increasing subsequence, considering each element to be its ending
        int ans = 1;
        for(int i=0;i<nums.length;i++){
            dp[i] = 1;
            for(int j=0;j<i;j++){
                if(nums[i]>nums[j]){
                    dp[i] = Math.max(dp[i],dp[j]+1); //here if the current element is lesser than the last element (that we consider on each iteration, then the max length ending at that last element will be either the current max + 1 or the max at the ending element)
                }
                ans = Math.max(dp[i],ans); //the ans is either the max at ending element or the ans max itself
            }
        }
        return ans;
    }
}
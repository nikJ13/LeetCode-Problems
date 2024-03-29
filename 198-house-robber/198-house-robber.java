class Solution {
    int dp[];
    public int helper(int[] nums, int index){
        if(index==nums.length-2 || index==nums.length-1){
            dp[index] = nums[index];
            return nums[index];
        }
        if(dp[index]!=-1){
            return dp[index];
        }
        for(int i=index+2;i<nums.length;i++){       
            dp[index] = Math.max(nums[index]+helper(nums,i),dp[index]); //check if the current steal+steal from other houses is greater than the steal specified in the dp array
        }
        return dp[index];
    }
    public int rob(int[] nums) {
        if(nums.length==1){
            return nums[0];
        }
        dp = new int[nums.length];
        int ans = 0;
        for(int i=0;i<nums.length;i++){ //initialize the dp array to '-1' each
            dp[i] = -1;
        }
        for(int j=0;j<nums.length;j++){ //with different starting points
            if(dp[j]==-1){
            ans = Math.max(helper(nums,j),ans);
            }
        }
        return ans;
    }
}
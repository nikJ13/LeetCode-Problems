class Solution {
   //oolean res = false;
    public boolean canJump(int[] nums) {
        if(nums.length==1){
            return true;
        }
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<=dp[i];j++){
                dp[j] = j + nums[j];
                if(dp[j]>=nums.length-1){
                    return true;
                }
            }
        }
        return false;
    }
}
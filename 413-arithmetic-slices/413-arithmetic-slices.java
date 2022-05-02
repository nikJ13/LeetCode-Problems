class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        int[] dp = new int[nums.length];
        int left = 0, diff = 0;
        for(int right=1;right<nums.length;right++){
            if(right==1){
                diff = nums[right] - nums[right-1];
            }else{
                if(diff!=nums[right]-nums[right-1]){
                    diff = nums[right]-nums[right-1];
                    dp[right] = dp[right-1];
                    left = right - 1;
                }else{
                    dp[right] = dp[right-1] + right - left - 1;
                }
            }
        }
        return dp[nums.length-1];
    }
}
class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int min=nums[0], max = nums[0], ans_min=nums[0], ans_max = nums[0], sum = nums[0];
        for(int i=1;i<nums.length;i++){
            min = Math.min(min+nums[i],nums[i]);
            max = Math.max(max+nums[i],nums[i]);
            ans_max = Math.max(ans_max,max);
            ans_min = Math.min(ans_min,min);
            sum = sum + nums[i];
        }
        if(sum-ans_min==0){
            return ans_max;
        }else{
            return Math.max(sum-ans_min,ans_max);
        }
    }
}
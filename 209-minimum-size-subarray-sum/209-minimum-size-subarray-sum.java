class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int start = 0,end = 0,sum = 0,ans = Integer.MAX_VALUE;
        while(end<nums.length){
            sum = sum + nums[end];
            while(start<=end && sum>=target){
                ans = Math.min(ans,end-start+1);
                sum = sum - nums[start];
                start++;
            }
            end++;
        }
        if(ans==Integer.MAX_VALUE){
            return 0;
        }
        return ans;
    }
}
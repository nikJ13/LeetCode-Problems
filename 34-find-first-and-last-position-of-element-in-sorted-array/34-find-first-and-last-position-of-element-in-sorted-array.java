class Solution {
    public int[] searchRange(int[] nums, int target) {
        int end = nums.length-1, ans_end = -1;
        int start = 0, ans_start = -1;
        while(start<nums.length){
            if(nums[start]==target){
                ans_start = start;
                break;
            }
            start++;
        }
        while(end>-1){
            if(nums[end]==target){
                ans_end = end;
                break;
            }
            end--;
        }
        int[] ans = new int[]{ans_start,ans_end};
        return ans;
    }
}
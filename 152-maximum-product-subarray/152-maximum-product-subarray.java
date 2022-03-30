class Solution {
    public int maxProduct(int[] nums) {
        int min = nums[0],max = nums[0],ans = nums[0], temp = 0;
        for(int i = 1;i<nums.length;i++){
            temp = min;
            min = Math.min(min*nums[i],Math.min(max*nums[i],nums[i]));
            max = Math.max(max*nums[i],Math.max(temp*nums[i],nums[i]));
            ans = Math.max(min,Math.max(max,ans));
        }
        return ans;
    }
}
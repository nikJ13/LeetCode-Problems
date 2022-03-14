class Solution {
    public int maxProduct(int[] nums) {
        int min = nums[0];
        int max = nums[0];
        int ans = nums[0];
        int temp;
        for (int i=1;i<nums.length;i++){
            temp = min;
            min = Math.min(min*nums[i],Math.min(max*nums[i],nums[i]));
            max = Math.max(max*nums[i],Math.max(temp*nums[i],nums[i]));
            ans = Math.max(ans,Math.max(min,max));
        }
        return ans;
    }
}
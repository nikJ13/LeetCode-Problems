class Solution {
    public int findMin(int[] nums) {
        int ans = nums[0];
        for(int i=1;i<nums.length;i++){
            if(nums[i]<nums[i-1]){
                ans = nums[i];
                break;
            }
        }
        return ans;
    }
}
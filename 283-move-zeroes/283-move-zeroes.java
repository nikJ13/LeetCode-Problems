class Solution {
    public void moveZeroes(int[] nums) {
        if(nums.length==1){
            return;
        }else{
        int left = 0;
        int right = 1;
        while(right<nums.length){
            if(nums[left]==0 && nums[right]!=0){
                nums[left] = nums[right];
                nums[right] = 0;
                left ++;
            }else if((nums[left]!=0 && nums[right]==0)||(nums[left]!=0 && nums[right]!=0)){
                left++;
            }
            right ++;
        }
        }
    }
}
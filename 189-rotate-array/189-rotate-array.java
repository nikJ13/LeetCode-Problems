class Solution {
    public void rotate(int[] nums, int k) {
        k = k%nums.length;
        int ind = nums.length - k;
        int left = ind;
        int right = nums.length - 1;
        int temp = 0;
        while(left<right){
            temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left ++;
            right --;
        }
        left = 0;
        right = ind-1;
        temp = 0;
        while(left<right){
            temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left ++;
            right --;
        }
        left = 0;
        right = nums.length-1;
        temp = 0;
        while(left<right){
            temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left ++;
            right --;
        }
        //return nums;
    }
}
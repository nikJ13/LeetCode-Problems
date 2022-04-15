class Solution {
    public int findMin(int[] nums) {
        int left=0,right=nums.length-1,flag = 0;
        if(nums[right]>nums[0]){ // if the whole array is sorted, then the last element will be greater than the first element of the array
            return nums[0];
        }
        while(left<right){ //using binary search
            int mid = left + (right-left)/2;
            if(nums[mid]<nums[0]){
                right = mid;
            }else if(nums[mid]>=nums[0]){
                left = mid+1;
            }
        }
        return nums[left];
    }
}
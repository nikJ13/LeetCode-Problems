class Solution {
    public int findPeakElement(int[] nums) {
        int left = 0, right = nums.length-1;
        while(left<right){ //using binary search; check if the current mid is greater than the element to the right of it or not
            int mid = left + (right-left)/2;
            if(nums[mid]<nums[mid+1]){ //if lesser, that means the peak has to be somewhere on the right of the mid element
                left = mid+1;
            }else{ //if greater than or equal to, then the peak has to be somewhere on the left (and including itself) of the mid element
                right = mid;
            }
        }
        return left;
    }
}
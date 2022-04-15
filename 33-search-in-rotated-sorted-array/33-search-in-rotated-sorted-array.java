class Solution {
    
    private int searchpivot(int[] nums){
        int left = 0, right = nums.length-1;
        while(left<right){
            int mid = left+(right-left)/2;
            if(nums[mid]>=nums[0]){
                left = mid + 1;
            }else{
                right = mid;
            }
        }
        return left;
    }
    private int binarysearch(int[] nums, int left, int right,int target){
        while(left<=right){
            int mid = left + (right-left)/2;
            if(nums[mid]==target){
                return mid;
            }else if(nums[mid]<target){
                left = mid+1;
            }else{
                right = mid - 1;
            }
        }
        return -1;
    }
    public int search(int[] nums, int target) {
        int pivot = searchpivot(nums);
        if(nums[pivot]==target){
            return pivot;
        }
        if(nums[pivot]<=target && nums[nums.length-1]>=target){
            return binarysearch(nums,pivot,nums.length-1,target);
        }else{
            return binarysearch(nums,0,pivot-1,target);
        }
    }
}
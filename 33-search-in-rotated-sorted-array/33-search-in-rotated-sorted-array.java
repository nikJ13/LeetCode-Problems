class Solution {
    public int binarySearch(int[] arr,int start,int end,int target){
        //int mid = start + (end-start)/2;
        while(start<=end){
            int mid = start + (end-start)/2;
            //System.out.println(start);
            //System.out.println(end);
            if(arr[mid]<target){
                start = mid+1;
            }else if(arr[mid]>target){
                end = mid-1;
            }else{
                return mid;
            }
        }
        return -1;
    }
    public int pivotFind(int[] arr){ // function to find the pivot element; the element which is the smallest in the array, after the array has been rotated
        int left = 0;
        int right = arr.length-1;
        //int mid = left + (right-left)/2;
        while(left<right){
            int mid = left + (right-left)/2;
            if(arr[mid]>=arr[0]){
                left = mid+1;
            }else{
                right = mid;
            }
        }
        return left;
    }
    public int search(int[] nums, int target) {
        int piv = pivotFind(nums);
        if(nums[piv]==target){
            return piv;
        }
        int n = nums.length-1;
        if(target>=nums[piv]&&target<=nums[n]){
            //System.out.println("here");
            return binarySearch(nums,piv,n,target);
        }else{
            return binarySearch(nums,0,piv-1,target);
        }
    }
}
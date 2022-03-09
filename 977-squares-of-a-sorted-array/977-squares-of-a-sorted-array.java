import java.util.*;
class Solution {
    public int[] sortedSquares(int[] nums) {
        int small = 0;
        for(int i=0;i<nums.length;i++){
            small = i;
            if(nums[i]>=0){
                break;
            }
        }
        int left = small-1;
        int right = small;
        int[] arr = new int[nums.length];
        int temp = 0;
        while(left>=0 && right<=nums.length-1){
            if(nums[left]*nums[left]>nums[right]*nums[right]){
                arr[temp] = nums[right]*nums[right];
                right++;
            }else{
                arr[temp] = nums[left]*nums[left];
                left--;
            }
            temp++;
        }
        while(left>=0){
            arr[temp++] = nums[left]*nums[left];
            left --;
        }
        while(right<=nums.length-1){
            arr[temp++] = nums[right]*nums[right];
            right ++;
        }
        return arr;
    }
}
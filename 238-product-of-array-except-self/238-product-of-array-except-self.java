class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] ans = new int[nums.length];
        ans[0] = 1;
        int temp = 0;
        for(int i=1;i<nums.length;i++){   //iterate from the front side, calculating the product of numbers before the current number 
            if(i==1){
                ans[i] = nums[i-1];
            }else{
                ans[i] = ans[i-1]*nums[i-1];
            }
        }
        for(int i=nums.length-1;i>=0;i--){ //iterate from the backside, calculating the product of numbers after the current number
            if(i==nums.length-1){
                temp = 1;
            }else{
            ans[i] = ans[i] * nums[i+1] * temp;
            temp = nums[i+1]*temp;
            }
        }
        return ans;
    }
}
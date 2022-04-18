class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<>();
        for(int i=0;i<nums.length-2;i++){
            if(i==0 || nums[i]!=nums[i-1]){
                int start = i+1;
                int end = nums.length-1;
                int new_sum = 0-nums[i];
                while(start<end){
                    // System.out.println("start");
                    // System.out.println(nums[i]);
                    // System.out.println(nums[start]);
                    // System.out.println(nums[end]);
                    // System.out.println("end");
                    if(nums[start]+nums[end]==new_sum){
                        List<Integer> temp_arr = new ArrayList<>();
                        temp_arr.add(nums[i]);
                        temp_arr.add(nums[start]);
                        temp_arr.add(nums[end]);
                        ans.add(temp_arr);
                        int temp = nums[end];
                        start++;
                        while(start<end && nums[end]==temp){
                            end--;
                        }
                    }else if(nums[start]+nums[end]<new_sum){
                        int temp = nums[start];
                        while(start<end && nums[start]==temp){
                            start++;
                        }
                    }else{
                        int temp = nums[end];
                        while(start<end && nums[end]==temp){
                            end--;
                        }
                    }
                }
            }
        }
        return ans;
    }
}
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> dict = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if(dict.containsKey(nums[i])){
                return true;
            }else{
                dict.put(nums[i],1);
            }
        }
        return false;
    }
}
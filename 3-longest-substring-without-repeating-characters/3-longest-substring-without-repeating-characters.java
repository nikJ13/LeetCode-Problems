class Solution {
    public int lengthOfLongestSubstring(String s) {
        //System.out.println(s.length());
        int[] arr = new int[128];
        int ans = 0, start = 0, count = 0;
        for(int end=0;end<s.length();end++){
            while(arr[s.charAt(end)]==1){
                arr[s.charAt(start)] = 0;
                start++;
                count--;
            }
            arr[s.charAt(end)] = 1;
            count++;
            ans = Math.max(ans,count);
        }
        return ans;
    }
}
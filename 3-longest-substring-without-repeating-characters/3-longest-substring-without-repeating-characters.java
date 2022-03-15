class Solution {
    public int lengthOfLongestSubstring(String s) {
        int ans=0;
        ArrayList<Character> arr = new ArrayList<>();
        for(int i=0;i<s.length();i++){
            while(arr.contains(s.charAt(i))){
                arr.remove(0);
            }
            arr.add(s.charAt(i));
            ans = Math.max(ans,arr.size());
        }
        return ans;
    }
}
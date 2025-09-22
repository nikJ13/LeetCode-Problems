class Solution {
    public int countSubstrings(String s) {
        int count = 0;
        for(int i=0;i<s.length();i++){
            //calculating odd palindromes
            int left=i-1,right=i+1;
            while(left>=0 && right<s.length() && s.charAt(left)==s.charAt(right)){
                count++;
                left--;
                right++;
            }

            //calculating even palindromes
            left=i; right=i+1;
            while(left>=0 && right<s.length() && s.charAt(left)==s.charAt(right)){
                count++;
                left--;
                right++;
            }
        }
        return count + s.length();
    }
}
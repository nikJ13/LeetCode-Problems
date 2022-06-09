class Solution {
    private boolean checkPalindrome(String s){
        int start = 0;
        int end = s.length()-1;
        while(start<=end){
            if(s.charAt(start)!=s.charAt(end)){
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
    public int removePalindromeSub(String s) {
        if(checkPalindrome(s)){
            return 1;
        }
        return 2;
    }
}
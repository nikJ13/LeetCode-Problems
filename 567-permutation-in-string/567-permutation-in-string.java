class Solution {
    public boolean match(int[] s1_map,int[] s2_map){  // match the arrays for each window
        for(int i=0;i<26;i++){
            if(s1_map[i]!=s2_map[i]){
                return false;
            }
        }
        return true;
    }
    public boolean checkInclusion(String s1, String s2) {
        if(s1.length()>s2.length()){
            return false;
        }
       int[] map1 = new int[26];
        int[] map2 = new int[26];
        for(int i=0;i<s1.length();i++){  // keeping the track of each char count in the first window
            map1[s1.charAt(i) - 'a']++; // this array is what needs to be matched
            map2[s2.charAt(i) - 'a']++;
        }
        int start = 0;
        for(int i=s1.length();i<s2.length();i++){
            if(match(map1,map2)){ // checks if the window in s1 matches the window in s2
                return true;
            }
            // here, moving the window by one character forward
            map2[s2.charAt(start)-'a']--; //removing the left most char in the window
            start++;
            map2[s2.charAt(i)-'a']++; //adding a new right most char in the window
        }
        return match(map1,map2); //match the last windows
    }
}
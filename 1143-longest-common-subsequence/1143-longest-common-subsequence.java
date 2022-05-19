class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int[][] dp = new int[text1.length()+1][text2.length()+1];
        for(int i=1;i<text1.length()+1;i++){
            for(int j=1;j<text2.length()+1;j++){
                //System.out.println(text1.charAt(i-1));
                //System.out.println(text1.charAt(j-1));
                if(text1.charAt(i-1)==text2.charAt(j-1)){
                    //System.out.println(dp[i-1][j-1]++);
                    dp[i][j] = ++dp[i-1][j-1];
                }else{
                    dp[i][j] = Math.max(dp[i-1][j],dp[i][j-1]);
                }
                //System.out.println(dp[i][j]);
            }
        }
        return dp[text1.length()][text2.length()];
    }
}
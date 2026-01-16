class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Problem: find the longest common subsequence
        Solution:
        Naive Approach => iterating through each string and checking if it equal and storing a count for it
        >O(n^2)
        
        Optimised appraoch =>
          "" a b c d e
        "" 0 0 0 0 0 0 
        a  0 1 1 1 1 1
        c  0 1 1 2 2 2
        e  0 1 1 2 2 3
        
          "" a b c a e
        "" 0 0 0 0 0 0 
        a  0 1 1 1 1 1
        flag = 0, 1
        a,a => 1
        a,ab => 1
        a,abc => 1
        a,abca => 
        
        "",abc
        a,
        
        comparing the characters which are at the column and row index
        
        num = max(dp[i-1][j],dp[i][j-1])
        
        if text1[j]==text2[i]:
            num += 1
        
        a,ab
        
        "",ab
        
        a,a
        
         a b c b a
        a1 1 1 1 1
        b1 2 2 2 2
        c1 2 3 3 3
        b1  
        c
        b
        a
        
        ab
        abcb
        
        a,abc => 1
        
        ab,abc => 
        a,abcb => 1
        
        
        
        """
        dp = [[0 for j in range(len(text1)+1)] for i in range(len(text2)+1)]
        #print(len(dp),len(dp[0]))
        for i in range(1,len(text2)+1):
            flag = 0
            # print(dp)
            for j in range(1,len(text1)+1):
                if text2[i-1]==text1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
        
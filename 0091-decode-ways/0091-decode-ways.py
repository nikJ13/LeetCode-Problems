class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Problem: find the number of ways to decode the expression
        Solution: hashmap = {Number: Letter}
        
        
        Example 1:

        Input: s = "12"
        Output: 2
        Explanation:
        "12" could be decoded as "AB" (1 2) or "L" (12).
        
        "12" (1+1)=> "1"(1),"12"(1)
        "1"=>"2"(1)

        Example 2:
        Input: s = "226"
        Output: 3
        Explanation:
        "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
        "226"(2+1)=>"2"(2),"22"(1)
        "2"(1+1)=>"2"(1),"26"(1)
        "2"(1)=>"6"(1)
        "6"(1)
            2 2 6
            1 2 3
        dp[i] = (check the validity of the current element) + (check the validity of the prev curr element; return dp[i-1])
        
         2 0 3
         1 1 1
        "03"=>
        203
        "203"(1)=>"2"(0),"20"(1)
        "2"(0)=>"0"(check validity;0),"03"(0)
        "20"(1)=>"3"(1)
        "2262342"
            2  22
        26 
        TC - O(N)
        H = logN
        SC - O(N)
        
        0 3
        0 
        if dp[i-1]=0:
            dp[i] = 0
            
        2 0 3
        1 1 1
        
        1 2 3
        12 3
        1 23
        1 2 3 4
        1 2 3 
        
        12 3
        2 2 6
        1 2
        """
        dp = [0 for i in range(len(s))]
        if 1<=int(s[0])<=9:
            dp[0] = 1
        for i in range(1,len(s)):
            if dp[i-1]==0:
                dp[i] = 0
            else:
                if 1<=int(s[i])<=9:
                    dp[i] += dp[i-1]
                if 10<=int(s[i-1:i+1])<=26:
                    if i-2<0:
                        dp[i] += 1
                    else:
                        dp[i] += dp[i-2]
        return dp[-1]
                
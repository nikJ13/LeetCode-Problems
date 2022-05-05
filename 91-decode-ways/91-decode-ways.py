class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*len(s)
        dp[0] = 1 if s[0]!="0" else 0
        for i in range(1,len(s)):
            if i==1:
                if int(s[i])>0 and int(s[i])<10:
                    dp[i] += dp[i-1]
                if int(s[i-1:i+1])>=10 and int(s[i-1:i+1])<=26:
                    dp[i] += 1
            else:
                if int(s[i])>0 and int(s[i])<10:
                    dp[i] += dp[i-1]
                if int(s[i-1:i+1])>=10 and int(s[i-1:i+1])<=26:
                    dp[i] += dp[i-2]
        return dp[-1]
                
                    
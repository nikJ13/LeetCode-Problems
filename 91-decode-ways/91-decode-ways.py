class Solution:
    def numDecodings(self, s: str) -> int:
        ans = 0
        n = len(s)
        dp = {len(s):1}
        def recurse(index):
            nonlocal ans
            if index in dp:
                return dp[index]
            if s[index]=="0":
                return 0
            p = recurse(index+1)
            if index+1<len(s) and (s[index]=="1" or (s[index]=="2" and s[index+1] in "0123456")):
                p += recurse(index+2)
            dp[index] = p
            return dp[index]
        return recurse(0)
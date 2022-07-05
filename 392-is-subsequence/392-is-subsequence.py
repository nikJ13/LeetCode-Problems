class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n,m = len(s),len(t)
        if m<n:
            return False
        if n==0:
            return True
        temp = 0
        for i in range(len(t)):
            if temp==len(s):
                return True
            if s[temp]==t[i]:
                temp += 1
        if temp==len(s):
            return True
        return False
                
        
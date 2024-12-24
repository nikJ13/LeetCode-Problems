class Solution:
    def gcd(n, m):
        start = min(n,m)
        while True:
            if n%start==0 and m%start==0:
                return start
            else:
                start -= 1

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        n = len(str1)
        m = len(str2)
        g = gcd(n,m)
        return str1[:g]
        

            
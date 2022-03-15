class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        ans = ""
        n = len(l)
        for i in range(n):
            ans = ans + l[i][::-1]
            if i!=n-1:
                ans = ans + " "
        return ans
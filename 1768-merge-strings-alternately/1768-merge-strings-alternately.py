class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        ans = ""
        for i in range(max(n,m)):
            if i<n:
                ans += word1[i]
            if i<m:
                ans += word2[i]
        return ans
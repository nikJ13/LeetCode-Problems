class Solution:
    
    def transform(self,s):
        dict1 = {}
        ans = []
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = i
            ans.append(str(dict1[s[i]]))
        return " ".join(ans)
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.transform(s)==self.transform(t)
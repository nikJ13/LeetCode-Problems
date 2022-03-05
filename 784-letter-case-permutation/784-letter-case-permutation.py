class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def recurse(temp,ind):
            if len(temp)==n:
                ans.append(temp)
                return
            if s[ind].isalpha():
                recurse(temp+s[ind].upper(),ind+1)
                recurse(temp+s[ind].lower(),ind+1)
            else:
                recurse(temp+s[ind],ind+1)
            
        ans = []
        n = len(s)
        recurse("",0)
        return ans
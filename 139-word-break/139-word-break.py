class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def helper(s):
            if not s:
                return True
            for word in wordDict:
                if word==s[:len(word)]:
                    if helper(s[len(word):]):
                        return True
            return False
        
        return helper(s)
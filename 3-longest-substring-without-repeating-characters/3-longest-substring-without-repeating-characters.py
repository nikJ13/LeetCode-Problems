class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n==0:
            return n
        dict1 = {s[0]:1}
        ans,count = 1,1
        i = 0
        j = 1
        while j<n:
            if s[j] not in dict1:
                dict1[s[j]] = 1
                count += 1
                j += 1
            else:
                ans = max(count,ans)
                count -= 1
                dict1.pop(s[i])
                i += 1
        ans = max(ans,count)
        return ans
        
        
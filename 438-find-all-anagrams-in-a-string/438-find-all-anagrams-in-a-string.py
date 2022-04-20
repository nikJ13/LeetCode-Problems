class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        alphas = [0]*26 # this array is for the string 'p'
        betas = [0]*26 # this array is for the string 's', while traversing the string
        ans = []
        
        #to compare if the two arrays are equal or not
        def isEqual(arr1,arr2):
            for i in range(26):
                if arr1[i]!=arr2[i]:
                    return False
            return True
        
        for char in p:
            alphas[ord(char)-ord("a")] += 1
        for i in range(len(p)-1):  # iterate the string 's' till window size as length of 'p' to find the freqeuncy of chrs in the first window
            betas[ord(s[i])-ord("a")] += 1
        start = 0
        end = len(p)-1
        while end<len(s):
            betas[ord(s[end])-ord("a")] += 1
            if isEqual(alphas,betas):
                ans.append(start)
            betas[ord(s[start])-ord("a")] -= 1
            start += 1
            end += 1
        return ans
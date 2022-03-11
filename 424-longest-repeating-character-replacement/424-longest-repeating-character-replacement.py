class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        ans = 0
        n = len(s)
        dict1 = {} # storing the frequeuncies of all the characters of the window
        for j in range(n):
            if s[j] not in dict1:    #checking if the rightmost character is there or not in the window dictonary
                dict1[s[j]] = 0
            dict1[s[j]] += 1
            if j-i+1-max(dict1.values())<=k:  #in each window, the number of times a particular character repeats should be maximum, so that there can be minimum number of replacements of disctinct characters, atmost k times; here, the length of the window is j-i+1 and so, the number of distinct values to be replaced is the expression given in the if condition
                ans = max(ans,j-i+1)
            else:
                dict1[s[i]] -= 1      # if the number of replacements exceeds 'k', then remove the leftmost character from the window and decrement the frequency count in the dictionary also
                if not dict1[s[i]]:  # if the character has zero frequency in the window, then just remove it
                    del dict1[s[i]]
                i += 1
        return ans
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        temp = {}
        ans = 1
        words = sorted(words,key = len)
        for word in words:
            temp[word] = 1
            for exclude_char in range(len(word)): #each character is iterated to consider it to be removed from the current word
                prev_temp = word[:exclude_char] + word[exclude_char+1:] #after excluding the particular char at the iteration, the rest of the remaining characters of the word form the predecessor
                if prev_temp in temp: # the predecessor is then searched for in the dictionary
                    temp[word] = max(temp[word],temp[prev_temp] + 1) # if present, then it equal to max count of chain ending at the current word
                    ans = max(ans,temp[word]) #updating the max chain ans for the whole array
        #print(temp)
        return ans
                
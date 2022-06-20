class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        temp = {}
        ans = 1
        words = sorted(words,key = len)
        for word in words:
            temp[word] = 1
            for exclude_char in range(len(word)):
                prev_temp = word[:exclude_char] + word[exclude_char+1:]
                if prev_temp in temp:
                    temp[word] = max(temp[word],temp[prev_temp] + 1)
                    ans = max(ans,temp[word])
        #print(temp)
        return ans
                
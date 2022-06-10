class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr = [0]*26
        start = 0
        ans = 0
        for end in range(len(s)):
            arr[ord(s[end])-65] += 1
            len_window = end-start+1
            distinct_count = len_window - max(arr)
            if distinct_count<=k:
                ans = max(ans,len_window)
            else:
                arr[ord(s[start])-65] -= 1
                start += 1
        return ans
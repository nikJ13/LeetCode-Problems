class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        max_f = float("-inf")
        for f in freq:
            if freq[f]>max_f:
                max_f = freq[f]
        ans = []
        curr_f = max_f
        while k>0:
            for f in freq:
                if freq[f]==curr_f and k>0:
                    k -= 1
                    ans.append(f)
            curr_f -= 1
        return ans
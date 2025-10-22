class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
        return sorted(nums, key=lambda x: (freq[x], -x))
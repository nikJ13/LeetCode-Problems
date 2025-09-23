class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        streak, ans = 0, 0
        for i in num_set:
            if i-1 not in num_set:
                streak = 1
                while i+1 in num_set:
                    i += 1
                    streak += 1
                
                ans = max(streak, ans)
        return ans
            
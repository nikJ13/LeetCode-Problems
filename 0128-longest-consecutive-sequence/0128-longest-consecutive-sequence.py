class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        streak = 0
        num_set = set(nums)

        for num in num_set:
            if num-1 not in num_set:
                curr_streak = 1
                curr_num = num

                while curr_num + 1 in num_set:
                    curr_streak += 1
                    curr_num += 1
                
                streak = max(streak, curr_streak)
        
        return streak
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        max_left, min_right = float("-inf"), float("inf")
        start, end = 0, -1
        for i in range(len(nums)):
            max_left = max(nums[i], max_left)
            if max_left > nums[i]:
                end = i
        
        for i in range(len(nums)-1,-1,-1):
            min_right = min(min_right, nums[i])
            if min_right < nums[i]:
                start = i
        print(start, end)
        return end - start + 1
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        max_val = float("-inf")
        min_val = float("inf")
        # basically, we check from left to right
        # whichever number is smaller than the max value
        # encountered, then that means that number is not at
        # the correct place and has to be sorted
        # hence, that can be a potential right boundary

        '''
        Whereas for right to left, we check what all values are bigger than the min_val encountered, that ways that number has to be sorted as the min_val from right to left would ideally be the largest value and anything greater than that means that the list is not sorted. Hence, that number could be the left boundary
        '''
        start, end = 0, 0
        for i in range(len(nums)):
            if nums[i]>=max_val:
                max_val = nums[i]
            else:
                end = i
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<=min_val:
                min_val = nums[i]
            else:
                start = i
        if end==0 and start==0:
            return 0
        return end - start + 1
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        quick sort is the one algo that can do this sorting in place

        2 3 8 4 6
          l     r
        2 6 8 4 3  
        """
        def calculate_pivots(start, end):
            if start >= end:
                return
            # we need to decide the pivots
            new_pivot_idx = iterations(start, end)
            calculate_pivots(start, new_pivot_idx-1)
            calculate_pivots(new_pivot_idx+1, end)
            return
        
        def iterations(start, end):
            left = start
            curr_pivot = nums[end]
            for right in range(start, end):
                if nums[right] <= curr_pivot:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
            nums[left], nums[end] = nums[end], nums[left]
            return left
        
        calculate_pivots(0,len(nums)-1)
        return nums
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        problem: what is the longest increasing subsequence
        
        solution:
        max_counter = 1
        iterate through the list[1:]
            if arr[i]>arr[i-1]:
                max_counter += 1
            
        [1,3,5,4,7]
                 *
        max_counter = 1,2,3,1,2
        ans = max_counter
        
        [7,6,5,4,3,2]
        
        [9,0,-2,3,-10]
                   *
        [3,0,6,2,4,7,0,0]
                       *
        ans = 2,3
        max_counter = 1,2,1,2,3,1
        """
        ans, max_counter = 1,1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                max_counter += 1
            else:
                ans = max(ans,max_counter)
                max_counter = 1
        ans = max(ans,max_counter)
        return ans
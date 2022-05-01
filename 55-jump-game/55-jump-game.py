class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start,destination = len(nums)-2,len(nums)-1 # this is greedy solution; here we take two pointers, and iterate from the back of the array
        # at each start pointer, we check if that can be reached to the destination pointer or not; if so, then this start pointer becomes the new destination and the element before it becomes the new start element; check the neetcode solution for it
        while start>=0:
            if start+nums[start]>=destination:
                destination = start
            start -= 1
        return destination==0
                
            
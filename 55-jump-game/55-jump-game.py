class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start,destination = len(nums)-2,len(nums)-1
        while start>=0:
            if start+nums[start]>=destination:
                destination = start
            start -= 1
        return destination==0
                
            
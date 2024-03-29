class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        neg = 0
        left = 0
        right = 0
        ans = 0
        # Expand your window (right pointer) until you hit 0 or end of list and then contract (left pointer) each time counting the number of negative entries. Count max length only when number of negatives is even. Repeat until all elements are scanned.
        while left<len(nums):
            while right<len(nums) and nums[right]!=0:
                if nums[right]<0:
                    neg += 1
                right += 1
                if neg%2==0:
                    ans = max(ans,right-left)
            while left<right:
                if nums[left]<0:
                    neg -= 1
                left += 1
                if neg%2==0:
                    ans = max(ans,right-left)
            right += 1
            left = right
        return ans
            
            
                
        
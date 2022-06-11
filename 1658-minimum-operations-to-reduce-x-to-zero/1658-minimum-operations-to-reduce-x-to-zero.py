class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        ans = -1
        start, sum1 = 0,0
        temp = sum(nums)
        for end in range(len(nums)):
            sum1+=nums[end]
            while start<=end and sum1>temp-x:
                sum1 -= nums[start]
                start += 1
            if sum1==temp-x:
                ans = max(ans,end-start+1)
        if ans==-1:
            return -1
        return len(nums)-ans
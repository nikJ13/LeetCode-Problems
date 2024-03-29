class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        diff,left = 0,0
        for right in range(1,len(nums)):
            if right==1:
                diff = nums[right]-nums[right-1]
            else:
                if diff!=nums[right]-nums[right-1]:
                    diff = nums[right]-nums[right-1]
                    left = right-1
                    dp[right] = dp[right-1]
                else:
                    dp[right] = dp[right-1] + right-left - 1
        return dp[-1]
        
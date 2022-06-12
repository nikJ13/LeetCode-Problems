class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start, ans, sum1 = 0,0,0
        dict1 = {num:0 for num in nums}
        for end in range(len(nums)):
            if dict1[nums[end]]==1:
                ans = max(ans,sum1)
                while dict1[nums[end]]==1:
                    sum1-=nums[start]
                    dict1[nums[start]] -= 1
                    start += 1
            dict1[nums[end]] += 1
            sum1 += nums[end]
        ans = max(ans,sum1)
        return ans
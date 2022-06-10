class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start, ans, sum1 = 0,0,0
        temp = []
        dict1 = {num:1 for num in nums}
        for end in range(len(nums)):
            if dict1[nums[end]]==2:
                ans = max(ans,sum1)
                while dict1[nums[end]]==2:
                    sum1-=nums[start]
                    dict1[nums[start]] -= 1
                    start += 1
            dict1[nums[end]] += 1
            sum1 += nums[end]
            #print(temp)
        ans = max(ans,sum1)
        return ans
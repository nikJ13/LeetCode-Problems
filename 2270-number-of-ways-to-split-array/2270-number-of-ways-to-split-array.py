class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # prefix and suffix sums
        # [a,b,c,d]
        # [a,a+b,a+b+c,a+b+c+d]
        # [a+b+c+d,b+c+d,c+d,d]
        # prefix_sum[i]>=suffix_sum[i]-curr[i]
        # total_sum - prefix = suffix_sum
        # then compare prefix_sum with suffix_sum
        total_sum = 0
        for i in range(len(nums)):
            total_sum += nums[i]
        ans = 0
        prefix_sum = 0
        for i in range(len(nums)-1):
            prefix_sum += nums[i]
            suffix_sum = total_sum - prefix_sum
            if prefix_sum>=suffix_sum:
                ans += 1
        return ans
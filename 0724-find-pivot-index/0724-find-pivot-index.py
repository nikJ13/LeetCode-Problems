class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summations = []
        sum1 = 0
        for i in nums:
            sum1 += i
            summations.append(sum1)
        max_sum = summations[-1]
        for j in range(len(nums)):
            pref_sum = summations[j] - nums[j]
            next_sum = max_sum - summations[j]
            if pref_sum == next_sum:
                return j
        return -1
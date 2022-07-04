class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        sumleft = 0
        for i in range(len(nums)):
            if sumleft == s - sumleft - nums[i]:
                return i
            sumleft += nums[i]
        return -1
        
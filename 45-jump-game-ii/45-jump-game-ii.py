class Solution:
    def jump(self, nums: List[int]) -> int:
        count, left, right = 0,0,0
        while right<len(nums)-1:
            farthest = 0
            for i in range(left,right+1):
                farthest = max(farthest,nums[i]+i)
            left = right + 1
            right = farthest
            count += 1
        return count
                
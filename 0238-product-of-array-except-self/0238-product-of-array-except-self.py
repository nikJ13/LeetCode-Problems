class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front = [1 for _ in range(len(nums))]
        back = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                continue
            if i == 1:
                front[i] = nums[i-1]
                continue
            front[i] = nums[i-1] * front[i-1]
        
        for j in range(len(nums)-1, -1, -1):
            if j == len(nums)-1:
                continue
            if j == len(nums)-2:
                back[j] = nums[j+1]
                continue
            back[j] = nums[j+1] * back[j+1]
        
        ans = []
        for k in range(len(nums)):
            ans.append(front[k] * back[k])
        
        return ans
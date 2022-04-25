class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(nums,index,temp):
            ans.append(temp[:])
            for i in range(index,len(nums)):
                temp.append(nums[i])
                helper(nums,i+1,temp)
                temp.pop()
        helper(nums,0,[])
        return ans
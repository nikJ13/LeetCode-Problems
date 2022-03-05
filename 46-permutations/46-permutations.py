class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def recurse(temp):
            if len(temp)==n:
                ans.append(temp[:])
                return
            for j in nums:
                if j not in temp:
                    temp.append(j)
                    recurse(temp)
                    temp.pop()
            
        n = len(nums)
        for i in nums:
            recurse([i])
        return ans
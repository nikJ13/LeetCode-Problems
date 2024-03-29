class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def helper(index,number,temp):
            if number==0:
                ans.append(temp[:])
                return
            if number<0:
                return
            for i in range(index,n):
                if number-candidates[i]<0:
                    continue
                temp.append(candidates[i])
                helper(i,number-candidates[i],temp)
                temp.pop()
        helper(0,target,[])
        return ans
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        
        def helper(index,arr,number,temp):
            if number==0:
                ans.append(temp[:])
                return
            for i in range(index,n):
                if (i!=index and arr[i]==arr[i-1]) or number-arr[i]<0:
                    continue
                temp.append(arr[i])
                helper(i+1,arr,number-arr[i],temp)
                temp.pop()
        candidates = sorted(candidates)
        helper(0,candidates,target,[])
        return ans
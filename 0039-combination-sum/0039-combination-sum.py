class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def helper(sum_arr, tar, start_idx):
            if tar==0:
                ans.append(sum_arr)
                return
            
            for c in range(start_idx, len(candidates)):
                if tar>=candidates[c]:
                    helper(sum_arr + [candidates[c]], tar - candidates[c], c)
            return
        
        helper([], target, 0)
        return ans

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def helper(idx, arr):
            if len(arr)==k:
                return arr
            for p in range(idx+1,n+1):
                if p not in visited:
                    visited.add(p)
                    tmp = helper(p, arr + [p])
                    if tmp is not None:
                        ans.append(tmp)
                    visited.remove(p)
        visited = set()
        for i in range(1,n+1):
            visited.add(i)
            temp = helper(i ,[i])
            if temp is not None:
                ans.append(temp)
            visited.remove(i)
        return ans
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        def helper(i, j):
            # print(i,j)
            if i<0 or i>=n or j<0 or j>=m or grid[i][j]==-1 or grid[i][j]==0:
                return 0
            grid[i][j] = -1
            temp = 1
            for x,y in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                temp += helper(x, y)
            return temp
        
        count = 0
        ans = 0
        for p in range(n):
            for q in range(m):
                if grid[p][q]==1:
                    count = helper(p, q)
                    ans = max(ans, count)
        return ans
            
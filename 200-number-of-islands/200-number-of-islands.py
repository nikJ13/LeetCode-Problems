class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def recurse(grid,i,j,n,m):
            if i<0 or i==n or j<0 or j==m or grid[i][j]=="-1" or grid[i][j]=="0":
                return
            grid[i][j] = "-1"
            recurse(grid,i+1,j,n,m)
            recurse(grid,i,j+1,n,m)
            recurse(grid,i-1,j,n,m)
            recurse(grid,i,j-1,n,m)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    recurse(grid,i,j,len(grid),len(grid[0]))
                    ans += 1
        return ans
                    
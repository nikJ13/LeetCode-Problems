class Solution {
    public int helper(int[][] grid, int x, int y, int n, int m){
        if(x>=n||y>=m||x<0||y<0||grid[x][y]==-1||grid[x][y]==0){
            return 0;
        }
        grid[x][y] = -1;
        return 1 + helper(grid,x+1,y,n,m) + helper(grid,x,y+1,n,m) + helper(grid,x-1,y,n,m) + helper(grid,x,y-1,n,m);
    }
    public int maxAreaOfIsland(int[][] grid) {
        int ans = 0;
        int n = grid.length;
        int m = grid[0].length;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]==1){
                    ans = Math.max(ans,helper(grid,i,j,n,m));
                }
            }
        }
        return ans;
    }
}
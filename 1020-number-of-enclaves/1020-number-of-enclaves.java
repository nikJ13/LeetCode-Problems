class Solution {
    public void helper(int[][] grid, int x, int y, int n, int m){
        if(x<0||x>=n||y<0||y>=m||grid[x][y]==0){
            return;
        }
        grid[x][y] = 0;
        helper(grid,x-1,y,n,m);
        helper(grid,x,y-1,n,m);
        helper(grid,x+1,y,n,m);
        helper(grid,x,y+1,n,m);
    }
    public int numEnclaves(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        for(int i=0;i<n;i++){
            if(grid[i][0]==1){
                helper(grid,i,0,n,m);
            }
            if(grid[i][m-1]==1){
                helper(grid,i,m-1,n,m);
            }
        }
        for(int i=0;i<m;i++){
            if(grid[0][i]==1){
                helper(grid,0,i,n,m);
            }
            if(grid[n-1][i]==1){
                helper(grid,n-1,i,n,m);
            }
        }
        int count = 0;
        for(int i=1;i<n-1;i++){
            for(int j=1;j<=m-1;j++){
                if(grid[i][j]==1){
                    count++;
                }
            }
        }
        return count;
    }
}
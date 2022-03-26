class Solution {
    public boolean helper(int[][] grid, int x, int y, int n, int m){
        //System.out.println(x+" "+y);
        if(grid[x][y]==1||grid[x][y]==-1){
            return true;
        }
        if(x==0||y==0||x==n-1||y==m-1){
            return false;
        }
        grid[x][y] = -1;
        boolean top = helper(grid,x-1,y,n,m); 
        boolean left = helper(grid,x,y-1,n,m);
        boolean bottom = helper(grid,x+1,y,n,m);
        boolean right = helper(grid,x,y+1,n,m);
        return top && left && right && bottom;
    }
    public int closedIsland(int[][] grid) {
        int ans = 0;
        int n = grid.length;
        int m = grid[0].length;
        boolean[][] visited = new boolean[n][m];
        for(int i=1;i<n-1;i++){
            for(int j=1;j<m-1;j++){
               //System.out.println(grid[i][j]);
                if(grid[i][j]==0){
                    if(helper(grid,i,j,n,m)){
                        //System.out.println(i+" "+j);
                        ans++;
                    }
                }
                //System.out.println(grid[i][j]);
            }
        }
        return ans;
    }
}
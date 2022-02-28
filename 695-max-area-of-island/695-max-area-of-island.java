class Solution {
    public static int dfs(int[][] visited,int[][] grid,int x,int y,int n,int m){
        if(x<0||x>=n||y<0||y>=m||visited[x][y]==1||grid[x][y]==0){
            return 0;
        }
        visited[x][y] = 1;
        return 1+dfs(visited,grid,x-1,y,n,m)+dfs(visited,grid,x,y-1,n,m)+dfs(visited,grid,x+1,y,n,m)+dfs(visited,grid,x,y+1,n,m);
    }
    public int maxAreaOfIsland(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int[][] visited = new int[n][m];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                visited[i][j] = 0;
            }
        }
        int ans = 0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(visited[i][j]==0 && grid[i][j]==1){
                    ans = Math.max(dfs(visited,grid,i,j,n,m),ans);
                }
            }
        }
        return ans;
    }
}
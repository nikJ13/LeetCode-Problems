class Solution {
    public void helper(int[][] grid2,int x,int y, int n, int m){
        if(x<0||x>=n||y<0||y>=m||grid2[x][y]==0){
            return;
        }
        grid2[x][y] = 0;
        helper(grid2,x-1,y,n,m);
        helper(grid2,x,y-1,n,m);
        helper(grid2,x+1,y,n,m);
        helper(grid2,x,y+1,n,m);
    }
    public int countSubIslands(int[][] grid1, int[][] grid2) {
        int n = grid1.length;
        int m = grid1[0].length;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid2[i][j]==1 && grid1[i][j]==0){
                    helper(grid2,i,j,n,m);
                }
            }
        }
        int count=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid2[i][j]==1){
                    helper(grid2,i,j,n,m);
                    count++;
                }
            }
        }
        return count;
    }
}
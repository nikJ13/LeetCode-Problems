class Solution {
    
    private void helper(char[][] grid, int x, int y, int m, int n){
        if(x<0||x>=m||y<0||y>=n||grid[x][y]=='0'||grid[x][y]=='2'){
            return;
        }
        grid[x][y] = '2';
        helper(grid,x+1,y,m,n);
        helper(grid,x,y+1,m,n);
        helper(grid,x-1,y,m,n);
        helper(grid,x,y-1,m,n);
    }
    public int numIslands(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int count = 0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]=='1'){
                    //System.out.println("hehe");
                    helper(grid,i,j,m,n);
                    count++;
                }
            }
        }
        return count;
    }
}
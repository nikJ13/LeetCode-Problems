class Solution {
    public void helper(char[][] grid,int x,int y,int n,int m){
        if(x<0 || x>=n || y<0 || y>=m || grid[x][y]=='2' || grid[x][y]=='0'){
            return;
        }
        grid[x][y] = '2';
        helper(grid,x+1,y,n,m);
        helper(grid,x,y+1,n,m);
        helper(grid,x-1,y,n,m);
        helper(grid,x,y-1,n,m);
    }
    public int numIslands(char[][] grid) {
        int count=0;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                //System.out.println(grid[i][j]);
                if(grid[i][j]=='1'){
                    //System.out.println("yes");
                    helper(grid,i,j,grid.length,grid[0].length);
                    count ++;
                }
            }
        }
        return count;
    }
}
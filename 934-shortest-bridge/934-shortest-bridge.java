class Solution {
    public void helper(int[][] grid, int x, int y, int n, int team){
        if(x<0||x>=n||y<0||y>=n||grid[x][y]!=1){
            return;
        }
        grid[x][y] = team;
        helper(grid,x-1,y,n,team);
        helper(grid,x,y-1,n,team);
        helper(grid,x+1,y,n,team);
        helper(grid,x,y+1,n,team);
    }
    public int shortestBridge(int[][] grid) {
        int n = grid.length;
        int count = 2;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==1){
                    helper(grid,i,j,n,count);
                    count ++;
                }
            }
        }
        //System.out.println(grid[0][1]+" "+grid[2][2]);
        Queue<int[]> queue=new LinkedList<>();
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==2){
                    queue.add(new int[]{i,j,0});
                }
            }
        }
        int[][] directions = new int[][]{{1,0},{0,1},{-1,0},{0,-1}};
        while(!queue.isEmpty()){
            int size = queue.size();
            for(int i=0;i<size;i++){
                int[] node = queue.remove();
                for(int j=0;j<4;j++){
                    int newX = node[0] + directions[j][0];
                    int newY = node[1] + directions[j][1];
                    if(newX<0||newX>=n||newY<0||newY>=n){
                        continue;
                    }
                    if(grid[newX][newY]==0){
                        queue.add(new int[]{newX,newY,node[2]+1});
                        grid[newX][newY] = 1;
                    }else if(grid[newX][newY]==3){
                        return node[2];
                    }
                }
            }
        }
        return -1;
    }
}
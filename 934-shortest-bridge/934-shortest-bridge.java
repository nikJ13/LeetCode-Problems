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
        for(int i=0;i<n;i++){   //marking both the islands with different colours (numbers i.e. '2' for the first island and '3' for the second one)
            for(int j=0;j<n;j++){
                if(grid[i][j]==1){
                    helper(grid,i,j,n,count);
                    count ++;
                }
            }
            if(count==4){
                break;
            }
        }
        // making a queue and initiliasing it with one of the island's cells; because we need to find the min distance between the first and the second island
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
                    if(newX<0||newX>=n||newY<0||newY>=n){ // checking the boundary conditions
                        continue;
                    }
                    if(grid[newX][newY]==0){   // we have to measure the distance between islands by traversing only the cells with '0'
                        queue.add(new int[]{newX,newY,node[2]+1});
                        grid[newX][newY] = 1; // marking this cell as visited
                    }else if(grid[newX][newY]==3){  // if the cell is equal to the other island, that means the other island has been found; return the node's distance
                        return node[2];
                    }
                }
            }
        }
        return -1;
    }
}
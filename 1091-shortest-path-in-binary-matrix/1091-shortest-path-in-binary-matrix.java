class Solution {
    int[][] directions = {{0,1},{1,0},{-1,0},{0,-1},{1,1},{-1,-1},{1,-1},{-1,1}};
    public int shortestPathBinaryMatrix(int[][] grid) {
        if(grid[0][0]==1){
            return -1;
        }
        Queue<int[]> que = new LinkedList<int[]>();
        int[][] direction = new int[][]{{0,1},{1,0},{0,-1},{-1,0},{1,1},{-1,-1},{1,-1},{-1,1}};
        que.add(new int[]{0,0,1});
        int n = grid.length;
        int m = grid[0].length;
        int[][] visited = new int[n][m];
        visited[0][0] = 1;
        while(!que.isEmpty()){
            int k = que.size();
            for(int i=0;i<k;i++){
                int[] node = que.poll();
                if(node[0]==n-1 && node[1]==m-1){
                    return node[2];
                }
                for(int j=0;j<8;j++){
                    int newX = node[0] + direction[j][0];
                    int newY = node[1] + direction[j][1];
                    int distance = node[2];
                    if(newX>=0 && newX<n && newY>=0 && newY<m && visited[newX][newY]!=1 && grid[newX][newY]==0){
                        visited[newX][newY] = 1;
                        que.add(new int[]{newX,newY,distance+1});
                    }
                }
            }
        }
        return -1;
    }
}
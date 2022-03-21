class Solution {
    public int maxDistance(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int[][] vis = new int[n][m];
        int ans = 0;
        int count = 0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                vis[i][j] = Integer.MAX_VALUE-100000;
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]==1){
                    vis[i][j] = 0;
                }else{
                    count++;
                    if(j>0){
                        vis[i][j] = Math.min(1 + vis[i][j-1],vis[i][j]);
                    }
                    if(i>0){
                        vis[i][j] = Math.min(1+vis[i-1][j],vis[i][j]);
                    }
                }
            }
        }
        if(count==n*m||count==0){
            return -1;
        }
        for(int i=n-1;i>=0;i--){
            for(int j=m-1;j>=0;j--){
                if(grid[i][j]==0){
                    if(j<m-1){
                        vis[i][j] = Math.min(1+vis[i][j+1],vis[i][j]);
                    }
                    if(i<n-1){
                        vis[i][j] = Math.min(1+vis[i+1][j],vis[i][j]);
                    }
                    ans = Math.max(ans,vis[i][j]);
                }
            }
        }
        return ans;
    }
}
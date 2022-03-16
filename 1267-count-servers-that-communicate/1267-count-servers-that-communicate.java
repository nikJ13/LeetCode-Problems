class Solution {
    public int countServers(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int[] measure_rows = new int[n];
        int[] measure_cols = new int[m];
        int ans=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]==1){
                    ans ++;
                    measure_rows[i]++;
                    measure_cols[j]++;
                }
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]==1 && measure_rows[i]==1 && measure_cols[j]==1){  //this checks if there are cells where the whole col and row has only one '1', which is in that particular cell
                    ans--;
                }
            }
        }
        return ans;
    }
}
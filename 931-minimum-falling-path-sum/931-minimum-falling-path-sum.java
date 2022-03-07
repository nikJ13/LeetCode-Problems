class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int cols = matrix[0].length;
        int rows = matrix.length;
        for(int i=1;i<rows;i++){
            for(int j=0;j<cols;j++){
                //System.out.println(cols);
                if(j==0){
                    matrix[i][j] += Math.min(matrix[i-1][j],matrix[i-1][j+1]);
                }else if(j==cols-1){
                    //System.out.println("here");
                    matrix[i][j] += Math.min(matrix[i-1][j-1],matrix[i-1][j]);
                }else{
                    matrix[i][j] += Math.min(matrix[i-1][j-1],Math.min(matrix[i-1][j],matrix[i-1][j+1]));
                }
            }
        }
        int ans = Integer.MAX_VALUE;
        for(int i=0;i<cols;i++){
            ans = Math.min(ans,matrix[rows-1][i]);
        }
        return ans;
    }
}
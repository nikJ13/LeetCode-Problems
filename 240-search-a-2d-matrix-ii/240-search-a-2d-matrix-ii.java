class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int x = 0, y = matrix[0].length-1;
        while(y>=0 && x<matrix.length){
            if(matrix[x][y]<target){
                x++;
            }else if(matrix[x][y]>target){
                y--;
            }else{
                return true;
            }
        }
        return false;
    }
}
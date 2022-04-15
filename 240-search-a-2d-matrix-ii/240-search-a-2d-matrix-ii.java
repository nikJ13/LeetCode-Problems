class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int x = 0, y = matrix[0].length-1;
        while(y>=0 && x<matrix.length){
            if(matrix[x][y]<target){ //first check row wise if the target element falls lesser than the greatest element in the current row
                x++;
            }else if(matrix[x][y]>target){ //if the target element is lesser than the greatest element in that particular row, then that means the ans must be in that row itself; thus, decrease the col index
                y--;
            }else{
                return true;
            }
        }
        return false;
    }
}
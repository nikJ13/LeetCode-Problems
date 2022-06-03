class NumMatrix {
    private int[][] arr;
    public NumMatrix(int[][] matrix) {
        for(int i=0;i<matrix.length;i++){
            int sum = 0;
            for(int j=0;j<matrix[0].length;j++){
                matrix[i][j] = sum + matrix[i][j];
                sum = matrix[i][j];
            }
        }
        arr = matrix;
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        if(col1==0){
            int sum = 0;
            for(int i=row1;i<=row2;i++){
                sum += arr[i][col2];
            }
            return sum;
        }else{
            int sum = 0;
            for(int i=row1;i<=row2;i++){
                sum += arr[i][col2] - arr[i][col1-1];
            }
            return sum;
        }
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */
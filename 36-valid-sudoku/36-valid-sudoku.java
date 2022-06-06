class Solution {
    
    private boolean checkSudoku(char[][] board, int startRow, int endRow, int startCol, int endCol){
        boolean[] arr = new boolean[10];
        for(int l=startRow; l<endRow; l++){
            for(int m=startCol; m<endCol; m++){
                if(board[l][m]=='.'){
                    continue;
                }
                if(arr[board[l][m] - '0']==true){
                    return true;
                }
                arr[board[l][m]-'0'] = true;
            }
        }
        return false;
    }
    public boolean isValidSudoku(char[][] board) {
        // checking the rows
        for(int i=0;i<9;i++){
            if(checkSudoku(board,i,i+1,0,9)) return false;
        }
        //checking the columns
        for(int i=0;i<9;i++){
            if(checkSudoku(board,0,9,i,i+1)) return false;
        }
        
        //checking the boxes
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                if(checkSudoku(board,i*3,(i+1)*3,j*3,(j+1)*3)) return false;
            }
        }
        return true;
    }
}
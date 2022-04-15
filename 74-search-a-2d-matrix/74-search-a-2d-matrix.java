class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length-1;
        int columns = matrix[0].length-1, ans_row = -1;
        for(int i=0;i<=rows;i++){
            if(matrix[i][columns]==target){
                return true;
            }else if(matrix[i][columns]>target){
                ans_row = i;
                break;
            }
        }
        if(ans_row==-1){
            return false;
        }
        int[] arr = matrix[ans_row];
        int left = 0, right = columns;
        while(left<=right){
            int mid = left + (right-left)/2;
            if(arr[mid]==target){
                return true;
            }else if(arr[mid]<target){
                left = mid + 1;
            }else if(arr[mid]>target){
                right = mid - 1;
            }
        }
        return false;
    }
}
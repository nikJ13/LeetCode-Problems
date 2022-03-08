class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int n = mat.length;
        int m = mat[0].length;
        if(n==0){
            return mat;
        }
        int[][] ans = new int[n][m];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                ans[i][j] = Integer.MAX_VALUE-100000;
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(mat[i][j]==0){
                    ans[i][j] = 0;
                }else{
                    if(i>0){
                        ans[i][j] = Math.min(ans[i][j],1 + ans[i-1][j]);
                    }
                    if(j>0){
                        ans[i][j] = Math.min(ans[i][j],1 + ans[i][j-1]);
                    }
                }
            }
        }
        //System.out.println(mat[2][0]);
        for(int i=n-1;i>=0;i--){
            for(int j=m-1;j>=0;j--){
                    if(i<n-1){
                        ans[i][j] = Math.min(ans[i][j],1 + ans[i+1][j]);
                    }
                    if(j<m-1){
                        ans[i][j] = Math.min(ans[i][j],1 + ans[i][j+1]);
                    }
            }
        }
        return ans;
    }
}
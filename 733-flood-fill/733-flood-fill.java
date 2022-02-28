class Solution {
    public static void recursive(int x, int y,int n,int m,int newColor,int color,int[][] image){
            if(x<0 || x>=n || y<0 || y>=m || image[x][y]!=color || image[x][y]==newColor){
                return;
            }
            image[x][y] = newColor;
            recursive(x+1,y,n,m,newColor,color,image);
            recursive(x,y+1,n,m,newColor,color,image);
            recursive(x-1,y,n,m,newColor,color,image);
            recursive(x,y-1,n,m,newColor,color,image);
        }
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int color = image[sr][sc];
        int n = image.length;
        int m = image[0].length;
        recursive(sr,sc,n,m,newColor,color,image);
        return image;
    }
}
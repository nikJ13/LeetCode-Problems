class Solution {
    public void helper(int[][] img, int x, int y, int n, int m, int oldColor, int newColor){
        if(x>=n || x<0 || y>=m || y<0 || img[x][y]!=oldColor || img[x][y]==newColor){
            return;
        }
        img[x][y] = newColor;
        helper(img,x+1,y,n,m,oldColor,newColor);
        helper(img,x,y+1,n,m,oldColor,newColor);
        helper(img,x-1,y,n,m,oldColor,newColor);
        helper(img,x,y-1,n,m,oldColor,newColor);
    }
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int oldColor = image[sr][sc];
        helper(image,sr,sc,image.length,image[0].length,oldColor,newColor);
        return image;
    }
}
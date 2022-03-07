class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int ans = Integer.MAX_VALUE;
        int cols;
        List<Integer> row;
        for(int i=1;i<triangle.size();i++){
            cols = triangle.get(i).size();
            row = triangle.get(i);
            for(int j=0;j<cols;j++){
                if(j==0){
                    row.set(j,row.get(j) + triangle.get(i-1).get(j));
                }else if(j==cols-1){
                    row.set(j,row.get(j) + triangle.get(i-1).get(j-1));
                }else{
                    row.set(j,row.get(j) + Math.min(triangle.get(i-1).get(j-1),triangle.get(i-1).get(j)));
                }
            }
        }
        for(int j = 0;j<triangle.size();j++){
            if(triangle.get(triangle.size()-1).get(j)<ans){
                ans = triangle.get(triangle.size()-1).get(j);
            }
        }
        return ans;
    }
}
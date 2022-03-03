class Solution {
    class Pair{
        int first;
        int second;
        public Pair(int first,int second){
            this.first = first;
            this.second = second;
        }
        int getf(){
            return this.first;
        }
        int gets(){
            return this.second;
        }
    }
    public int orangesRotting(int[][] grid) {
        int count = 0;
        int k = 0;
        int flag = 0;
        LinkedList<Pair> que = new LinkedList<Pair>();
        ArrayList<Pair> directions = new ArrayList<Pair>();
        directions.add(new Pair(1,0));
        directions.add(new Pair(0,1));
        directions.add(new Pair(-1,0));
        directions.add(new Pair(0,-1));
        int n = grid.length;
        int m = grid[0].length;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]==2){
                    que.add(new Pair(i,j));
                }
            }
        }
        //System.out.println(directions);
        Pair node = new Pair(0,0);
        while(que.size()!=0){
            k = que.size();
            //System.out.println(que);
            //System.out.println(count);
            for(int i=0;i<k;i++){
                node = que.poll();
                //System.out.println(node.first);
                for(int j=0;j<4;j++){
                    //System.out.println(directions.get(j).first);
                    int newRow = node.first + directions.get(j).first;
                    int newCol = node.second + directions.get(j).second;
                    if(newRow<0||newRow>=n||newCol<0||newCol>=m||grid[newRow][newCol]==2||grid[newRow][newCol]==0){
                        continue;
                    }
                    grid[newRow][newCol]=2;
                    que.add(new Pair(newRow,newCol));
                }
            }
            //System.out.println(que);
            if(que.size()!=0){count++;}
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]==1){
                    flag = 1;
                    //System.out.println("here");
                    break;
                }
            }
        }
        if(flag==1){return -1;}else{return count;}
    }
}
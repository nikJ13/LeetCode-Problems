class Solution {
    public void helper(List<List<Integer>> rooms, int index, boolean[] vis){
        //System.out.println(index);
        //System.out.println(vis[index]);
        if(rooms.get(index).size()==0||vis[index]==true){
            vis[index] = true;
            return;
        }
        vis[index] = true;
        for(int i=0;i<rooms.get(index).size();i++){
            //vis[rooms.get(index).get(i)] = true;
            helper(rooms, rooms.get(index).get(i),vis);
        }
    }
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        boolean[] vis = new boolean[rooms.size()];
        //vis[0] = true;
        helper(rooms,0,vis);
        for(int i=0;i<vis.length;i++){
            if(vis[i]==false){
                return false;
            }
        }
        return true;
    }
}
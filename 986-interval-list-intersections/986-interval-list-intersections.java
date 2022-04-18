class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        if(firstList.length==0 || secondList.length==0){
            return new int[0][0];
        }
        int first_ptr = 0, second_ptr = 0;
        List<int[]> ans = new ArrayList<>();
        while(first_ptr<firstList.length && second_ptr<secondList.length){
            int lower = Math.max(firstList[first_ptr][0],secondList[second_ptr][0]);
            int upper = Math.min(firstList[first_ptr][1],secondList[second_ptr][1]);
            if(lower<=upper){
                int[] temp = new int[]{lower,upper};
                ans.add(temp);
            }
            if(firstList[first_ptr][1]<secondList[second_ptr][1]){
                first_ptr++;
            }else{
                second_ptr++;
            }
        }
        return ans.toArray(new int[ans.size()][2]);
    }
}
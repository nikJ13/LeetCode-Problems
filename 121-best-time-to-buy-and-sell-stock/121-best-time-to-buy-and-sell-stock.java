class Solution {
    public int maxProfit(int[] prices) {
        int ans = 0;
        int first = prices[0], second = 0;
        for(int i=1;i<prices.length;i++){
            if(prices[i]<first){
                first = prices[i];
                second = 0;
            }
            if(prices[i]>second){
                second = prices[i];
            }
            ans = Math.max(ans,second-first);
        }
        return ans;
    }
}
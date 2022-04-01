class Solution {
    public int maxProfit(int[] prices) {
        int ans = 0;
        int min = 100000;
        for(int i=0;i<prices.length;i++){
            if(prices[i]<min){
                min = prices[i];
            }else{
                ans = ans + prices[i]-min;
                min = prices[i];
            }
        }
        return ans;
    }
}
class Solution {
    public static int recurse(int n, int[] arr){
        if(n==1){
            return 1;
        }else if(n<0){
            return 0;
        }
        if(arr[n]!=0){
            return arr[n];
        }
        //System.out.println(n);
        arr[n] = recurse(n-1,arr) + recurse(n-2,arr);
        return arr[n];
    }
    public int climbStairs(int n) {
        int[] arr = new int[n+1];
        for(int i=1;i<=n;i++){
            if(i==1){
                arr[i] = 1;
            }else if(i==2){
                arr[i] = 2;
            }else{
                arr[i] = 0;
            }
        }
        int a = recurse(n,arr);
        return a;
    }
}
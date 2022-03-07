class Solution {
    public boolean isPowerOfTwo(int n) {
        if(n==0){return false;}
        long m = (long) n;
        return (m&-m)==m;
    }
}
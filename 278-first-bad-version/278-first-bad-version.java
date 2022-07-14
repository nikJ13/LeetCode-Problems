/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int left = 1, right = n;
        // basic logic is that you first make sure that the right pointer becomes good, then that is where the condition loop breaks, thus, the ans is the left pointer
        while(left<=right){
            int mid = left + (right-left)/2;
            if(isBadVersion(mid)){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        return left;
    }
}
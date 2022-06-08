class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int ptr1 = m-1;
        int ptr2 = n-1;
        for(int i=n+m-1;i>=0;i--){
            if(ptr2<0){
                break;
            }
            if(ptr1>=0 && nums1[ptr1]>nums2[ptr2]){
                nums1[i] = nums1[ptr1];
                ptr1--;
            }else{
                nums1[i] = nums2[ptr2];
                ptr2--;
            }
        }
    }
}
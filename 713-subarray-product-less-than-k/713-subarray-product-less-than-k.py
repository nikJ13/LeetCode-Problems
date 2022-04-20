class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start,end,prod = 0,0,1
        n = len(nums)
        ans = 0
        while end<n:
            prod = prod * nums[end]
            while prod>=k and start<=end: #check if the product till the end pointer is greater than k or not; if true, then reduce the window size and the prod variable accordingly
                prod = prod//nums[start]
                start += 1
            ans += end-start+1
            end += 1
        return ans
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        start, end = 1, max(candies)

        def check(arr, value):
            total_kids = 0
            for pile in arr:
                total_kids += pile//value
            return total_kids>=k

        max_val = 0
        while start<=end:
            mid = (start+end)//2
            valid = check(candies, mid)
            # print(mid)
            # print(valid)
            if valid:
                max_val = mid
                start = mid + 1
            else:
                end = mid - 1
        
        return max_val
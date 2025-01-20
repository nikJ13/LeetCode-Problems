class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(num,arr):
            count = 0
            for i in arr:
                count += ceil(i/num)
            return count
        ans = float("inf")
        start = 1
        end = max(piles)
        while start<=end:
            mid = (start + end)//2
            print(start, end , mid)
            out = helper(mid, piles)
            print(out)
            if out > h:
                start = mid + 1
            elif out <= h:
                ans = mid
                end = mid - 1
        return ans
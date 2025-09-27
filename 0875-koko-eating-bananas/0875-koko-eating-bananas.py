class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)

        def helper(num, piles):
            hours = 0
            for i in piles:
                hours += ceil(i/num)
            return hours
        ans = 0
        while start<=end:
            mid = (start + end) // 2
            res = helper(mid, piles)
            if res <= h:
                ans = mid
                end = mid - 1
            elif res > h:
                start = mid + 1
        return ans
    
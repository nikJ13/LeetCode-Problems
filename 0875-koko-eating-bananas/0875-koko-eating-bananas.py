class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)

        def check(mid, piles):
            ans = 0
            for p in piles:
                ans += ceil(p/mid)
            return ans
        res = 0
        while start<=end:
            mid = (start+end)//2
            val = check(mid, piles)
            if h>=val:
                res = mid
                end = mid - 1
            elif h<val:
                start = mid + 1
        return res


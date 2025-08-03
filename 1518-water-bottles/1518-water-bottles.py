class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        num = numBottles
        ans = num
        while num>=numExchange:
            q = num // numExchange
            ans += q
            r = num % numExchange
            left = q + r
            num = left
        return ans
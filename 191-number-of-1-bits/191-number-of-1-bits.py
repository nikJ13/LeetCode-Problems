class Solution:
    def hammingWeight(self, n: int) -> int:
        count,right = 0,0
        while n:
            right = n & 1
            if right==1:
                count += 1
            n = n >> 1
        return count
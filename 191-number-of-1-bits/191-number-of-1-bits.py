class Solution:
    def hammingWeight(self, n: int) -> int:
        count,right = 0,0
        while n:
            count += (n & 1)   # taking the right most bit of the binary number
            n = n >> 1  # right shifting by one
        return count
class Solution:
    def reverseBits(self, n: int) -> int:
        ans,zeros = 0,31
        while n:
            ans += (n&1) << zeros  # here, n&1 is used to get the rightmost bit of n and to reverse it, '31' number of zeros have to be placed to the right of it. Thus, the right most bit is left shifted with 31 (because 32 bit integer it is) number of zeroes to its right
            n = n >> 1  # right shifting all the bits to the right by one
            zeros -= 1  # decrementing the count of number of zeros by one
        return ans
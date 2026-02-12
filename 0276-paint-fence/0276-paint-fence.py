class Solution:
    def numWays(self, n: int, k: int) -> int:
        """
        Problem: we need to find the different combinations of colouring n posts such that 3 or more consecutive posts cannot be coloured the same
        Solution: need to break the problem down
        n = 3; k = 2
        for n=1 => 2
        for n=2 => 2x2
        for n=3 => 
        #1 if k>n
        #2 if k<n
        1 2 3 4
        bruteforce approach is to use an array of size n and colour them based on combinations and count from bottom up fashion
        DP Approach:
        we maintain two dp arrays: same and diff
        to populate same[i], we need to just take diff[i-1] coz if we take same[i-1], then that means the fence at i-2 would be same as i-1 and so we cant have i to be same coz three places
        to populate diff[i], we need to do same[i-1]*(k-1) [since there are k-1 different options for the current fence to be painted differently] and diff[i-1]*(k-1) [since there are k-1 different options again to be painted differently]
        """
        same, diff = [0]*n, [0]*n
        same[0], diff[0] = k, k
        if n==1:
            return same[-1]
        same[1] = k
        diff[1] = k*(k-1)
        for i in range(2,n):
            same[i] = diff[i-1]
            diff[i] = (same[i-1]+diff[i-1])*(k-1)
        return same[-1]+diff[-1]
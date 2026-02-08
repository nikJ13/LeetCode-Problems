class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Problem: min number of jumps to reach the index n-1
        Solution:
        Divide the problem into subproblems,
        [2,3,1,1,4]
        [(0,0),(1,1),(1,2),(2,2+1),(2,1+3)]

        2 =>0
        3 => if current idx is smaller than i-1 + nums[i-1]; 1 < 0+2
        1 => 2 < 1 + 3
        what is the min number of jumps to reach 0
        to reach 1
        to reach 2
        to reach 3
        to reach 4

        We can use two pointers, the right pointer iterates through the array till it reaches the end of a particular jump, marking all those elements it has traversed as 1 jump; when it reaches that, then increment the left pointer and also the jump counts being assigned by 1; so now we compare if the smallest jump count is what it has got by default or what it has gotten allocated
        [2,3,1,1,4]
        [0,1,1,2,2]
           *     *
        jc = 3

        we are saying that within a particular range, you will have those many jumps
        all the values within that range would have jumps[left] + 1 number of jumps
        """
        left, right = 0, 1
        jumps = [float("inf") for _ in range(len(nums))]
        jumps[0] = 0
        while right<len(nums):
            if right<=left+nums[left]: # if within that range
                while right<len(nums) and right<=left+nums[left]:
                    if jumps[left]+1<jumps[right]:
                        jumps[right] = jumps[left]+1
                    right += 1
            left += 1
        return jumps[-1]


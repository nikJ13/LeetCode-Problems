class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_val = float("-inf")
        count = 0
        for i in range(len(arr)):
            max_val = max(max_val, arr[i])
            if i==max_val:
                count += 1
        return count
        
        # 0 1 4 3 2

        # arr = 4 3 2 1 0
        # pos = 4 3 2 1 0
        # num = 0, 1
        # idx = 3
        # min_idx = 3 
        # max_idx = 4
        # count = 1, 2, 

        # arr = 1 0 2 3 4

        # pos = 1 0 2 3 4
        # num = 0, 1, 2, 3
        # idx = 3
        # min_idx = 1
        # max_idx = 3
        # count = 3
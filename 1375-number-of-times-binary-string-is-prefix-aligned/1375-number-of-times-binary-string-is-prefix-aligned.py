class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        # basically, we need to iterate through the flips array and see whether at a particular position in the flip array, all the numbers smaller than the flip number at that position have been already traversed through or not
        # so ideally, the max element should be present
        count = 0
        max_val = float("-inf")
        for i in range(len(flips)):
            max_val = max(max_val, flips[i])
            if i+1==max_val:
                count += 1
        
        return count
        

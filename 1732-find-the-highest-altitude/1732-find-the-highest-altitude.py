class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_h = 0
        curr_h = 0
        for i in gain:
            curr_h += i
            max_h = max(max_h,curr_h)
        return max_h
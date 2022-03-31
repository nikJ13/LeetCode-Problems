class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        visit = [0]*len(values)
        left_best = values[0] + 0
        ans = left_best + values[1] - 1
        for curr in range(2,len(values)):
            left_best = max(left_best,values[curr-1]+curr-1)
            ans = max(ans,left_best+values[curr]-curr)
        return ans
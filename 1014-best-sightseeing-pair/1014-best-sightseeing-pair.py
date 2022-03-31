class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        #left_best element is the element that is the most max element (which comprises of value at a particular index + that particular index) to the left of the current index 
        left_best = values[0] + 0 # calculating the elft_best element for index 1
        ans = left_best + values[1] - 1 # initialising the ans variable according to the given equation in the question, which is greatest element to the left of the current index + current index value - current index
        for curr in range(2,len(values)):
            left_best = max(left_best,values[curr-1]+curr-1) # the left_best element can either be the existing left_best element or the value at the index before the current index + previous index
            ans = max(ans,left_best+values[curr]-curr) # ans can be either the existing ans or the current left_best element + value at current index - current index
        return ans
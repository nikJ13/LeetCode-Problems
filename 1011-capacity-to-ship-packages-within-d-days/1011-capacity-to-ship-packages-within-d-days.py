class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start, end = max(weights), sum(weights)
        min_w = end
        def check(num):
            count = 0
            curr_sum = 0
            for w in weights:
                curr_sum += w
                if curr_sum>num:
                    count += 1
                    curr_sum = w
            if count+1<=days:
                return True
            return False
        
        while start<=end:
            mid = (start+end)//2
            print(mid)
            if check(mid):
                print("in")
                min_w = mid
                end = mid - 1
            else:
                start = mid + 1
        return min_w
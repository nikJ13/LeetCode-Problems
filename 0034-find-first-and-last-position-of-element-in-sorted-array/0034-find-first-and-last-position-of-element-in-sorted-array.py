class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums)-1
        ind = []
        while start<=end:
            print("start", start)
            print("end", end)
            mid = (start+end) // 2
            if target>=nums[mid]:
                if nums[mid]==target:
                    ind.append(mid)
                start = mid + 1
            elif target<nums[mid]:
                end = mid - 1
        if len(ind)==0:
            return [-1,-1]
        min_ind = min(ind)
        max_ind = max(ind)
        print(ind)
        while min_ind>=0 and nums[min_ind]==target:
            min_ind -= 1
        while max_ind<len(nums) and nums[max_ind]==target:
            max_ind += 1
        return [min_ind+1, max_ind-1]
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)-1
        flag = 0

        def search(start,end):
            while start<=end:
                mid = (start+end)//2
                if nums[mid]==target:
                    return True
                elif nums[mid]<target:
                    start = mid + 1
                else:
                    end = mid - 1
            return False

        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                left, right = i-1, i
                flag = 1
                break
        
        if left==0 and right==len(nums)-1 and flag==0:
            return search(left,right)
        left_ans = search(0,left)
        right_ans = search(right,len(nums)-1)

        return left_ans if left_ans else right_ans

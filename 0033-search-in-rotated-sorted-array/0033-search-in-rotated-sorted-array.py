class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # search for start and end ptrs

        # [1,3,5]
        # 
        left,right = 0,len(nums)-1
        def search(start,end):
            while start<=end:
                mid = (start+end)//2
                print("mid:",mid)
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    start = mid + 1
                else:
                    end = mid-1
                #print(start,end)
            return -1
        
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                left, right = i-1,i
                break
        if left==0 and right==len(nums)-1:
            return search(left, right)
        left_ans = search(0,left)
        right_ans = search(right,len(nums)-1)
        if left_ans!=-1:
            return left_ans
        else:
            return right_ans
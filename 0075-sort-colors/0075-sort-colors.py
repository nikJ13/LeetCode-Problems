class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quick_sort(arr,left,right):
            if right<=left:
                return
            # TODO

            pivot_idx = calculate_partition(arr,left,right)

            quick_sort(arr,left,pivot_idx-1)

            quick_sort(arr,pivot_idx+1,right)

            return arr

        def calculate_partition(arr,left,right):
            pivot = arr[right]
            i = left

            for j in range(left,right):
                if arr[j]<=pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            
            # swap the pivot with the element at the ith idx
            arr[i], arr[right] = arr[right], arr[i]
            return i

        return quick_sort(nums,0,len(nums)-1)



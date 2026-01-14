class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        """
        Problem: sort the colors in place
        Solution: Naive => applying the sort function (not allowed)
        Merge Sort => Divide the arr into multiple sub arrays and then within each pair we can switch the elements according to the order
        [2,0,2,1,1,0]
        find some number that is the smallest
        considers a pivot (which we can declare as the last element)
        we take two pointers i and j
        we increase j:
            we check if the number at j is smaller than equal to the number at pivot
            if it is:
                switch j and i
                and bring i = j
        finally when j reaches the pivot:
            we switch the number at i with the pivot
            
        [2,0,2,1,1,0]
        [0,2,2,1,1,0]
        i = 0th, 1st
        j = 0th, 1st, 2nd
        pivot = 5th
        """
        def quick_sort(arr,left,right):
            # base condition
            if left>=right:
                return
            pivot_index = partition(arr,left,right)
            
            quick_sort(arr, left, pivot_index-1)
            quick_sort(arr, pivot_index, right)
            
        
        def partition(arr,left,right):
            pivot = arr[right]
            i = left # to track smaller element
            
            # move all elements smaller than the pivot to the left
            for j in range(left,right): # iterating till one element before pivot
                if arr[j]<=pivot:
                    arr[i], arr[j] = arr[j], arr[i] # switch i and j numbers
                    i += 1
            
            arr[i], arr[right] = arr[right], arr[i]
            
            return i # return the position at which the pivot is after sorting the array
        
        ans = quick_sort(nums,0,len(nums)-1)
        return ans
        
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        temp1 = set(nums1) - set(nums2)
        temp2 = set(nums2) - set(nums1)
        return [list(temp1), list(temp2)]
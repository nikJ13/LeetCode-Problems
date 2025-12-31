# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        dict1 = {}
        curr = head
        while curr:
            if curr.val not in dict1:
                dict1[curr.val] = 0
            dict1[curr.val] += 1
            curr = curr.next
        
        prev = ListNode(-1)
        ans = prev
        curr = head
        while curr:
            if dict1[curr.val]==1:
                prev.next = curr
                prev = curr

            curr = curr.next
        prev.next = None
        return ans.next
            
        
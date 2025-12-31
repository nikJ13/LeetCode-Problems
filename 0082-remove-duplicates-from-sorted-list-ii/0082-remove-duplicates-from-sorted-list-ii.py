# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        flag = 0
        prev = ListNode(-1)
        ans = prev
        curr = head
        while curr:
            print(prev.val)
            flag = 0
            while curr.next and curr.next.val==curr.val:
                curr = curr.next
                flag = 1
            if flag==0:
                prev.next = curr
                prev = curr
            curr = curr.next
        if flag==1:
            prev.next = None
        return ans.next

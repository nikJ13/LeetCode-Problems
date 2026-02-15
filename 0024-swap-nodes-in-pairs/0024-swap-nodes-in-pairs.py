# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we need a pointer to the previous node so that we can keep track of the iteration
        """
        [1,2,3,4]
            sp p c
        counter = 4   
        prev = head
        curr's next = curr.next
        curr.next = prev
        prev.next = curr's next
        curr = curr's next
        counter += 1
        """
        if not head or not head.next:
            return head
        prev = head
        super_prev = ListNode(-1)
        super_prev.next = prev
        curr = head.next
        counter = 2
        ans = None
        while curr:
            if counter%2==0:
                if ans is None:
                    ans = curr
                curr_next = curr.next
                curr.next = prev
                prev.next = curr_next
                super_prev.next = curr
                curr = curr_next
                super_prev = super_prev.next
            else:
                curr = curr.next
                prev = prev.next
                super_prev = super_prev.next
            counter += 1
        return ans


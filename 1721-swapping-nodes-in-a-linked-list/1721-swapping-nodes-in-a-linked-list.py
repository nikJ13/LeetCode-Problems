# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow,fast = head,head
        count = 1
        vall = 0
        ans1,ans2 = None,None
        for _ in range(k-1):
            slow = slow.next
        ans1 = slow
        fast = slow
        slow = head
        while fast.next!=None:
            slow = slow.next
            fast = fast.next
            #print(fast.val)
        ans2 = slow
        ans1.val,ans2.val = ans2.val,ans1.val
        return head
        
        
        
                
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        node = head
        ans_list = []
        count = 0
        while node:
            ans_list.append(node.val)
            count += 1
            node = node.next
        ans = 0
        for s in ans_list:
            ans += s*(2**(count-1))
            count -= 1
        return ans
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        counter = 0
        for node in lists:
            if node:
                counter += 1
                pq.append((node.val, counter, node))
        heapq.heapify(pq)
        head_before = ListNode()
        prev = head_before
        while pq:
            # print(pq)
            value, c, node_ = heapq.heappop(pq)
            curr = ListNode(value)
            prev.next = curr
            prev = prev.next
            if node_.next != None:
                heapq.heappush(pq, (node_.next.val, c, node_.next))
        return head_before.next
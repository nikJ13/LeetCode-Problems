# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # make a dict with keys being the head of each linked list and value as the index in the bigger list
        # maintain a heapq and pop the smallest elements
        # add the head of that same linked list in the heapq

        # [[1,2,2],[1,1,2]]
        #     .         .
        if len(lists)==0:
            return None
        queue = []
        for i in range(len(lists)):
            linked_head = lists[i]
            if linked_head:
                queue.append((linked_head.val,i))
        heapq.heapify(queue)
        temp = ListNode(-1)
        curr = temp
        while len(queue)!=0:
            #print(queue)
            smallest_head, idx = heapq.heappop(queue)
            smallest_head_lc = lists[idx]
            if smallest_head_lc.next is not None:
                heapq.heappush(queue,(smallest_head_lc.next.val,idx))
            lists[idx] = smallest_head_lc.next
            smallest_head_lc.next = None
            curr.next = smallest_head_lc
            curr = curr.next
        return temp.next
        
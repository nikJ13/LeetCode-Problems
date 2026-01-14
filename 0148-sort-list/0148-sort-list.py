# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        # [4,2,1,3]

        # mid = 1
        # head_r = 3=>none
        # 4=>2=>1=>none
        # mid = 2
        # 4=>2=>none
        # 1 => none
        # 
        def finding_middle_node(node):
            slow, fast = node, node.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def mergesort(node):
            # TODO: Basecase
            # if there is only one element
            if not node or node.next is None:
                return node

            # finding the middle
            curr_middle = finding_middle_node(node)

            head_r = curr_middle.next
            curr_middle.next = None
            # getting nodes from the left and dividing further
            head_left = mergesort(node)
            # getting nodes from the right and dividing further
            head_right = mergesort(head_r)

            merged_head = merge(head_left, head_right)

            return merged_head


        def merge(head1, head2):
            # merge two sorted linked lists
            tmp = ListNode(float("-inf"))
            curr = tmp
            while head1 and head2:
                if head1.val<head2.val:
                    curr.next = head1
                    head1 = head1.next
                else:
                    curr.next = head2
                    head2 = head2.next
                curr = curr.next
            if head1:
                curr.next = head1
            else:
                curr.next = head2
            return tmp.next
        
        return mergesort(head)

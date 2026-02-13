"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Problem: make a copy of the whole structure
        Solution:
        Keep track of the positions of the nodes in a dictionary for O(1) lookup
        """
        old_curr = head
        dict_node = {}
        count = 0
        new_head = Node(-1)
        new_curr = new_head
        while old_curr is not None:
            # make a new node with the value of the curr_node
            # shift the curr_node to next node
            new_curr.next = Node(old_curr.val)
            new_curr = new_curr.next
            dict_node[old_curr] = new_curr
            old_curr = old_curr.next
        new_head = new_head.next
        new_curr = new_head
        old_curr = head

        # need to map the random node to new node's address

        # dictionary stores which random node it is pointing to
        while new_curr is not None:
            if old_curr.random is not None:
                new_curr.random = dict_node[old_curr.random]
            new_curr = new_curr.next
            old_curr = old_curr.next
        return new_head
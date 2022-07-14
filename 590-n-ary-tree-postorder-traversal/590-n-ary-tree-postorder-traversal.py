"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def recurse(node):
            if node:
                for i in range(len(node.children)):
                    recurse(node.children[i])
                ans.append(node.val)
        recurse(root)
        return ans
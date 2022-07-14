"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        def recurse(node):
            nonlocal ans
            if node:
                ans.append(node.val)
                for i in range(len(node.children)):
                    recurse(node.children[i])
        recurse(root)
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def recurse(leftsub,rightsub,node):
            if not node:
                return True
            if node.val>=rightsub or node.val<=leftsub:
                return False
            l = recurse(leftsub,node.val,node.left) # going to left subtree
            r = recurse(node.val,rightsub,node.right) # going to right subtree
            return l and r
        return recurse(float("-inf"),float("inf"),root)
        
                
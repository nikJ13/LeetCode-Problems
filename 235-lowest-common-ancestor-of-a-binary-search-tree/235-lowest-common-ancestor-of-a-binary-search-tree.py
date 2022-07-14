# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def recurse(node):
            # if not node:
            #     return None
            #print(node.val)
            if node:
                if node.val==p.val or node.val==q.val:
                    #print("here")
                    return node
                l,r = 0,0
                if node.left:
                    l = recurse(node.left)
                if node.right:
                    r = recurse(node.right)
                if l and r:
                    return node
                else:
                    return l or r
        return recurse(root)
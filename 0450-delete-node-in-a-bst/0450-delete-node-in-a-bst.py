# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        def helper(node, key):
            if node:
                if node.val==key:
                    if not node.left:
                        return node.right
                    if not node.right:
                        return node.left
                    successor = get_max(node.left)
                    node.val = successor.val
                    node.left = helper(node.left, successor.val)

                if node.val<key:
                    node.right = helper(node.right, key)
                else:
                    node.left = helper(node.left, key)

                return node

        def get_max(node):
            if not node.right:
                return node
            else:
                return get_max(node.right)
    
        return helper(root, key)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        """
                1
              2
            3
          4     
        """
        left_path_arr, right_path_arr, leaves_arr = [], [], []
        def left_path(node):
            if node:
                if node.left is None and node.right is None:
                    return
                left_path_arr.append(node)
                if node.left is not None:
                    left_path(node.left)
                else:
                    left_path(node.right)
        # [1,2,3,4]
        def right_path(node):
            if node:
                if node.left is None and node.right is None:
                    return
                right_path_arr.append(node)
                if node.right is not None:
                    right_path(node.right)
                else:
                    right_path(node.left)
        # [1,2,3,4]
        def leaves(node):
            if node:
                if node.left is None and node.right is None:
                    leaves_arr.append(node)
                if node.left is not None:
                    leaves(node.left)
                if node.right is not None:
                    leaves(node.right)
        # [4]
        left_path(root.left)
        right_path(root.right)
        leaves(root.left)
        leaves(root.right)
        ans = []
        ans.append(root.val)
        for node in left_path_arr:
            ans.append(node.val)
        # ans = [1,2,3,4]
        for i in range(len(leaves_arr)):
            ans.append(leaves_arr[i].val)
        # ans = [1,2,3,4]
        for i in range(len(right_path_arr)-1,-1,-1):
            ans.append(right_path_arr[i].val)
        return ans

                



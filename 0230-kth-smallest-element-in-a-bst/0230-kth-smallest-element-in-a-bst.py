# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 1
        ans = -1
        def helper(node):
            nonlocal counter, ans
            if ans!=-1:
                return
            if node:
                helper(node.left)
                if counter == k:
                    ans = node.val
                    print(ans)
                    counter += 1
                    return
                counter += 1
                helper(node.right)
        helper(root)
        return ans


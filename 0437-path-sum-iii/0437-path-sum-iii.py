# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        paths = defaultdict(int)
        count = 0
        def dfs(node, cumsum):
            nonlocal count
            if node:
                
                cumsum += node.val

                if cumsum == targetSum:
                    count += 1
                
                count += paths[cumsum - targetSum]
                paths[cumsum] += 1
                # print(paths)
                # print(cumsum)
                dfs(node.left, cumsum)
                dfs(node.right, cumsum)
                paths[cumsum] -= 1
        
        dfs(root, 0)
        return count
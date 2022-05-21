# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = [root]
        count = 0
        ans = []
        while que:
            k = len(que)
            temp = []
            for i in range(k):
                if count%2==0:
                    a = que.pop(0)
                    temp.append(a.val)
                    if a.left:
                        que.append(a.left)
                    if a.right:
                        que.append(a.right)
                else:
                    a = que.pop()
                    temp.append(a.val)
                    if a.right:
                        que.insert(0,a.right)
                    if a.left:
                        que.insert(0,a.left)
            count+=1
            ans.append(temp)
        return ans
                
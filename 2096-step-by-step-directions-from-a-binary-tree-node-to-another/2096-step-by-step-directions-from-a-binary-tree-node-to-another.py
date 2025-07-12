# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        startpath = []
        destpath = []
        def getPath(node,path,value):
            if not node:
                return False
            
            if node.val==value:
                return True
            
            path.append("L")
            if getPath(node.left,path,value):
                return True
            path.pop()

            path.append("R")
            if getPath(node.right,path,value):
                return True
            path.pop()

            return False
        getPath(root,startpath,startValue)
        getPath(root,destpath,destValue)

        i = 0
        while (i<len(startpath)) and (i<len(destpath)) and startpath[i]==destpath[i]:
            i += 1
        
        up_moves = "U" * (len(startpath)-i)
        down_moves = ''.join(destpath[i:])

        return up_moves + down_moves

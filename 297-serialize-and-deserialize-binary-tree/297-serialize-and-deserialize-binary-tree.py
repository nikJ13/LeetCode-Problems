# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = ""
        def recurse(node):
            nonlocal ans
            if not node:
                ans += ","
                return
            ans += str(node.val)+","
            recurse(node.left)
            recurse(node.right)
        recurse(root)
        return ans
        
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        que = data.split(",")
        def recurse(q):
            node = q.pop(0)
            if not node:
                return
            curr = TreeNode(int(node))
            curr.left = recurse(q)
            curr.right = recurse(q)
            return curr
        return recurse(que)
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
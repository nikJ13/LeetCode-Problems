"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        newvisited = {}
        def cloning(curr_node):
            # print(newvisited)
            if not curr_node.neighbors:
                return Node(curr_node.val,None)
            value = curr_node.val
            newneighs = []
            newNode = Node(value)
            newvisited[curr_node] = newNode
            for n in curr_node.neighbors:
                if n not in newvisited:
                    newvisited[n] = cloning(n)
                newneighs.append(newvisited[n])
            newvisited[curr_node].neighbors = newneighs
            return newvisited[curr_node]
        res = cloning(node)
        return res


        
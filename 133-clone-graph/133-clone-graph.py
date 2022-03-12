"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node==None:
            return None
        def dfs(vertex):
            nonlocal store
            curr = Node(vertex.val,[])
            store[curr.val] = curr # marks the current node as visited
            for i in range(len(vertex.neighbors)):
                if vertex.neighbors[i].val in store:  # checks if the neighbor of the vertex has already been visited or not
                    curr.neighbors.append(store[vertex.neighbors[i].val])
                else:
                    curr.neighbors.append(dfs(vertex.neighbors[i]))
            return curr
        store = {} # used to store the addresses of the visited nodes; the key is the visited node value and the value is the address
        return dfs(node)
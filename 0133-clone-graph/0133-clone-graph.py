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
        #print(node)
        if node==None:
            #print("here")
            return node
        visited = {}
        #print(here)
        # iterate through each node
        # on the way make new nodes and the graph for it
        copy_head = Node(node.val)
        que = [(node,copy_head)]
        visited[node] = copy_head
        while que:
            curr_node, copy_node = que.pop(0)
            # check if current node is in visited list
            # if curr_node in visited:
            #     continue
            for neighs in curr_node.neighbors:
                # check if the neighbors are already visited or not
                if neighs not in visited:
                    # make a new copy of the neighbor
                    copy_neighs = Node(neighs.val)
                    # add this neighbor to visited
                    visited[neighs] = copy_neighs
                    # add the neighbor and its copy to the que
                    que.append((neighs, copy_neighs))
                # add this copy as a neighbor of the copy_node
                copy_node.neighbors.append(visited[neighs])
        return copy_head
    
    # 1-> 2,4
    # for each neigh of 1, if neigh is not in visited, that means there are no copy neighs formed yet
    # so you make a copy neigh of a neigh and add the neigh to the visited node
    # add this neigh to the que
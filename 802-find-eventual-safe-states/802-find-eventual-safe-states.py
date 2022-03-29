class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = [0]*len(graph)
        ans = []
        cycle = set()
        safe = set()
        def recurse(node,vis):
            if node in cycle: # if the node is already in the cycle set, then return false
                return False
            if node in safe:  # if the node is already in the safe set, then that means it is not part of a cycle, thus, can return true
                return True
            if len(graph[node])==0: #if node is terminal, then add it to the safe set and return true
                safe.add(node)
                return True
            if vis[node]==1: # if the node is already visited, that means a cycle has been detected
                cycle.add(node)
                return False
            vis[node] = 1  # marking the node as visited
            for i in range(len(graph[node])): # for each neighbour of the node
                if not recurse(graph[node][i],vis):  # if there is a cycle detected, then add the current node also as a part of the cycle
                    cycle.add(node)
                    return False
            safe.add(node)  # this means that the node is safe as there is no cycle detected and return true
            return True
            
        for j in range(len(graph)):  #iterate each node in normal ascending order and check if the node is part of the cycle or safe set
            if recurse(j,visited):
                ans.append(j)  # if the node is part of the safe set , then add it to the answer array
        return ans
        
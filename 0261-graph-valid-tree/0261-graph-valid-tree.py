class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Need to identify the condition that a graph is a tree
        So one node is connected directly or indirectly to all nodes
        And there should be leaves, and there cant be cycles
        Perform a dfs from each node and keep track of the visited
        if it encounters an already visited node, then it is not a tree
        """
        if n==1:
            return True
        adj = {i:[] for i in range(n)}

        for edge in edges:
            start, end = edge
            if start not in adj:
                adj[start] = []
            adj[start].append(end)
            if end not in adj:
                adj[end] = []
            adj[end].append(start)
        
        def dfs(node,visited,parent):
            if len(adj[node])==0:
                return True
            if node in visited:
                return False
            visited.add(node)
            temp = True
            for child in adj[node]:
                if child!=parent:
                    temp &= dfs(child,visited,node)
            return temp
        
        for i in range(n):
            visited = set()
            if not dfs(i,visited,-1) or len(visited)!=n:
                return False
        return True


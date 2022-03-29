class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = [0]*len(graph)
        ans = []
        cycle = set()
        safe = set()
        def recurse(node,vis):
            if node in cycle:
                return False
            if node in safe:
                return True
            if len(graph[node])==0: #if node is terminal
                safe.add(node)
                return True
            if vis[node]==1:
                cycle.add(node)
                return False
            vis[node] = 1
            for i in range(len(graph[node])):
                if not recurse(graph[node][i],vis):
                    vis[node] = 0
                    cycle.add(node)
                    return False
            vis[node] = 0
            safe.add(node)
            return True
            
        for j in range(len(graph)):
            if recurse(j,visited):
                ans.append(j)
        return ans
        
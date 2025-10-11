class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        
        adj = {i:[] for i in range(n)}
        degree = [0] * n
        for edge in edges:
            v1, v2 = edge[0], edge[1]
            adj[v1].append(v2)
            adj[v2].append(v1)
            degree[v1] += 1
            degree[v2] += 1
        
        que = deque()
        for d in range(len(degree)):
            if degree[d] == 1:
                que.append(d)
        remaining = n
        while remaining>2:
            k = len(que)
            remaining -= k
            for _ in range(k):
                node = que.popleft()
                for neighs in adj[node]:
                    degree[neighs] -= 1
                    if degree[neighs] == 1:
                        que.append(neighs)
        return list(que)
        
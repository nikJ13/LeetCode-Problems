class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        adj = {i:[] for i in range(n)}
        indegree = [0 for _ in range(n)]
        for edge in edges:
            prev, next_ = edge[0], edge[1]
            adj[prev].append(next_)
            adj[next_].append(prev)
            indegree[prev] += 1
            indegree[next_] += 1
        
        que = deque([i for i in range(len(indegree)) if indegree[i]==1])
        remaining = n
        layers = 0
        while remaining>2:
            k = len(que)
            layers += 1
            remaining -= k
            for _ in range(k):
                node = que.popleft()
                for neighs in adj[node]:
                    indegree[neighs] -= 1
                    if indegree[neighs]==1:
                        que.append(neighs)
        return 2*layers if remaining<2 else 2*layers + 1

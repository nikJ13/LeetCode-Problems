import heapq
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        adj = {k:[] for k in range(1,n+1)}
        for a,b,w in edges:
            adj[a].append((b,w))
            adj[b].append((a,w))
        
        distances = [float("inf") for _ in range(n+1)]
        MOD = 10**9 + 7
        distances[n] = 0
        pq = [(0,n)]

        while pq:
            weight, node = heapq.heappop(pq)
            if distances[node]<weight:
                continue
            for neighs, weighs in adj[node]:
                if distances[neighs] > weight + weighs:
                    distances[neighs] = weight + weighs
                    heapq.heappush(pq, (distances[neighs], neighs))

        mem = {}
        def dfs(v):
            count = 0
            if v==n:
                return 1
            if v in mem:
                return mem[v]
            for neighs, weighs in adj[v]:
                if distances[neighs]<distances[v]:
                    count += dfs(neighs)
            mem[v] = count % MOD
            return mem[v]
        return dfs(1)


        
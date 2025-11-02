class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            indegree[v] += 1
        
        que = deque([i for i in range(n) if indegree[i]==0])
        ans = [set() for _ in range(n)]
        # print(que)
        while que:
            node = que.popleft()
            for neighs in adj[node]:
                indegree[neighs] -= 1
                if indegree[neighs]==0:
                    que.append(neighs)
                ans[neighs].update(ans[node])
                ans[neighs].add(node)
        for i in range(len(ans)):
            ans[i] = sorted(list(ans[i]))
        return ans
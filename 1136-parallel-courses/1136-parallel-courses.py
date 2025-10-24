class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = {k:[] for k in range(1, n+1)}
        indegree = [0 for i in range(n+1)]
        for r in relations:
            prev, next_n = r[0],r[1]
            adj[prev].append(next_n)
            indegree[next_n] += 1
        que = deque([i for i in range(1,n+1) if indegree[i]==0])
        ans = 0
        while que:
            k = len(que)
            for _ in range(k):
                node = que.popleft()
                for neighs in adj[node]:
                    indegree[neighs] -= 1
                    if indegree[neighs]==0:
                        que.append(neighs)
            ans += 1
        for i in indegree:
            if i!=0:
                return -1
        return ans
                    
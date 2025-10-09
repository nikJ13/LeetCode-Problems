class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [_ for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        adj = {i:[] for i in range(numCourses)}
        for trans in prerequisites:
            indegree[trans[0]] += 1
            if trans[1] not in adj:
                adj[trans[1]] = []
            adj[trans[1]].append(trans[0])
        que = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                que.append(i)
        res = []
        while que:
            node = que.popleft()
            for neighs in adj[node]:
                indegree[neighs] -= 1
                if indegree[neighs]==0:
                    que.append(neighs)
            res.append(node)
        if len(res)!=numCourses:
            return []
        return res
                
            

            

        
        

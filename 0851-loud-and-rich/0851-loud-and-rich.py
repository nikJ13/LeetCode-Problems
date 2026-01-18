from collections import deque
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        """
        Goal: x << (a,b,c,d,e)
        find the quietest person
        ans[x] = c
        for i in range(0,n):
            graph where parents are richer than children
            we could iterate through all the nodes that occur before x
            while visiting the parents of x, we can keep a counter of the parent that is the quietest
            once we visit all the parents of x, we exit the loop
            get the value y for a certain x
        
        adj = {keys (richer), values [(poorer)]}
        indegree = [0....(n-1)]
        """
        n = len(quiet)
        adj = {i:[] for i in range(n)}
        indegree = [0 for _ in range(n)]
        for edges in richer:
            rich, poor = edges
            if rich not in adj:
                adj[rich] = []
            adj[rich].append(poor)
            indegree[poor] += 1
        
        # the nodes where the indegrees are 0 (the richest people)
        ans = [0 for _ in range(n)]
        queue = []
        visited = set()
        for i in range(n):
            ans[i] = i
            if indegree[i]==0:
                queue.append((i,i))
                visited.add(i)
        queue = deque(queue)
        
        while queue:
            node, quietest_idx = queue.popleft()
            # iterate through all its children
            for child in adj[node]:
                indegree[child]-=1
                if child not in visited:
                    # check if the current quietest node for the child is quieter than the parent's quietest node
                    if quiet[quietest_idx]<quiet[ans[child]]:
                        ans[child] = quietest_idx
                    if indegree[child]==0:
                        queue.append((child, ans[child]))
            visited.add(node)
            # ans[node] = quietest_idx
        """
        ,(3,4),(3,5),(3,6)
        
        (1,2)
        """
        return ans
            
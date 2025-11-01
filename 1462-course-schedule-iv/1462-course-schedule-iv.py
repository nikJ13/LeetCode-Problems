class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]
        for prev, next_node in prerequisites:
            adj[prev].append(next_node)
            indegrees[next_node] += 1


        def check_pre(next_one, queue, visited):
            found = 0
            while queue:
                k = len(queue)
                for _ in range(k):
                    node = queue.popleft()
                    if node==next_one:
                        return True
                    for neighs in adj[node]:
                        if neighs not in visited:
                            visited.add(neighs)
                            queue.append(neighs)
            return False
                        
                    
        ans = []
        for prev_q, next_q in queries:
            temp = indegrees[:] # this makes a new copy of the list because when you slice, python essentially creates new strides for the slice and then makes a new copy of a compact array in the memory.
            que = deque([prev_q])
            visited = set()
            visited.add(prev_q)
            ans.append(check_pre(next_q, que, visited))
        
        return ans
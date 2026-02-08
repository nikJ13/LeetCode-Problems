from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        indegree = [0 for _ in range(numCourses)]
        for edges in prerequisites:
            parent, child = edges[1],edges[0]
            adj[parent].append(child)
            indegree[child] += 1
        """
        [[1,0],[1,2],[0,1]]
        0->1
        2->1
        1->0
        [1,1,0]
        [2]
        """
        # we need to find which courses are parents of all courses; indegree of 0
        queue = deque([i for i in range(numCourses) if indegree[i]==0])
        print(queue)
        visited = set()
        ans = []
        while queue:
            course = queue.popleft()
            if course in visited:
                return []
            for child in adj[course]:
                indegree[child] -= 1
                if indegree[child]==0:
                    queue.append(child)
            visited.add(course)
            ans.append(course)
        if len(ans)!=numCourses:
            return []
        return ans
            


from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Question: true if all courses can be done; else false
        
        Solution: adj_outgoing[parent] =[children] # key = course to be taken first
        incoming edges = [0,1]
        
        0
        
        0 -> 1
        
        0 -> 1
        1 -> 0
        
        0 -> 1 -> 2
             3 -> 2
        
        0 -> 1 -> 2
             2 -> 1
        0->1->2->3
              3->2
        indegree = [0,1,1]
        visited = [0]
        queue = [start with all the nodes that have zero incoming edges]
        visited = set()
        while queue:
            node = dequeue.popleft
            detecting a cycle
            if node is in visited:
                return False
                
            for children of node:
                decrease the number of incoming edges to a particular child
                if incoming edges for that particular child is equal to zero:
                    then we know that all its parents have been visited
                    add the child to the queue
                    add the child to visited
        return True
        """
        adj = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses
        for edges in prerequisites:
            a,b = edges
            adj[b].append(a)
            indegree[a] += 1
        
        queue = [i for i in range(numCourses) if indegree[i]==0]
        
        if len(queue)==0:
            return False
        print(adj)
        dq = deque(queue)
        visited = set()
        # print(dq)
        # print(indegree)
        # if you encounter another visited
        while dq:
            node = dq.popleft()
            if node in visited:
                return False
            for child in adj[node]:
                if child not in visited:
                    indegree[child] -= 1
                    if indegree[child]==0: # checking if all its parents are visited
                        dq.append(child)
            visited.add(node)
        if len(visited)==numCourses:
            return True
        else:
            return False
                    
                
            
        
        
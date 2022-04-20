class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int: # this is a variant of the number of islands problem
        n = len(isConnected)
        dict1 = {i:[] for i in range(n)} # making an adjacency map
        matrix = isConnected
        
        def helper(dict1,visited,vertex):
            if visited[vertex]==1 or len(dict1[vertex])==0: # edge case where, the vertex does not have any neighbors or that the vertex has already been visited
                return
            visited[vertex] = 1 # marking the current vertex as visited
            for neighbor in dict1[vertex]: # visiting each neighbor of the current vertex
                if(visited[neighbor]==0): # optimising condition, where each neighbor is checked if it is already visited before pushing it into another recursive call
                    helper(dict1,visited,neighbor)

        for i in range(n):
            for j in range(n):
                if i!=j and matrix[i][j]==1: #iterating through the matrix, to map each vertex to its list of neighbors
                    dict1[i].append(j)
                    dict1[j].append(i)
        visited = [0]*n # making a visited array, which will be constantly updated at the time of iterating through the adjacency map
        ans = 0
        for vertex in dict1: 
            if visited[vertex]==0: # if the vertex is not visited, then implement the recursive call, where each and every neighbor of the connected vertices are visited until all those are visited
                helper(dict1,visited,vertex)
                ans += 1 # then increment the ans counter by one
        return ans
                
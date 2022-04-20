class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dict1 = {i:[] for i in range(n)}
        matrix = isConnected
        
        def helper(dict1,visited,vertex):
            if visited[vertex]==1 or len(dict1[vertex])==0:
                return
            visited[vertex] = 1
            for neighbor in dict1[vertex]:
                if(visited[neighbor]==0):
                    helper(dict1,visited,neighbor)
        for i in range(n):
            for j in range(n):
                if i!=j and matrix[i][j]==1:
                    dict1[i].append(j)
                    dict1[j].append(i)
        visited = [0]*n
        ans = 0
        for vertex in dict1:
            if visited[vertex]==0:
                helper(dict1,visited,vertex)
                ans += 1
        return ans
                
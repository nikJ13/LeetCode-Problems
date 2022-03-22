class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1
        moves = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        n = len(grid)
        visited = [[-1 for _ in range(n)] for i in range(n)]
        visited[0][0],que = 1,[(0,0)]
        while que:
            node = que.pop(0)
            for i in range(8):
                if node[0]+moves[i][0]<0 or node[0]+moves[i][0]>=n or node[1]+moves[i][1]<0 or node[1]+moves[i][1]>=n or grid[node[0]+moves[i][0]][node[1]+moves[i][1]]==1:
                    continue
                if visited[node[0]+moves[i][0]][node[1]+moves[i][1]]==-1:
                    visited[node[0]+moves[i][0]][node[1]+moves[i][1]] = visited[node[0]][node[1]] + 1
                    que.append((node[0]+moves[i][0],node[1]+moves[i][1]))
        return visited[n-1][n-1]
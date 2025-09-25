class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        start = 0
        count_one = 0
        que = []
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    count_one = 1
                if grid[i][j]==2:
                    que.append((i,j))
        if count_one==0 and not que:
            return 0
        if not que:
            return -1
        count = 0
        while que:
            k = len(que)
            for _ in range(k):
                node = que.pop(0)
                if node[0] - 1 >= 0 and grid[node[0]-1][node[1]]!=2 and grid[node[0]-1][node[1]]!=0:
                    grid[node[0]-1][node[1]] = 2
                    que.append((node[0]-1,node[1]))
                if node[1]-1>=0 and grid[node[0]][node[1]-1]!=2 and grid[node[0]][node[1]-1]!=0:
                    grid[node[0]][node[1]-1] = 2
                    que.append((node[0],node[1]-1))
                if node[0]+1<n and grid[node[0]+1][node[1]]!=2 and grid[node[0]+1][node[1]]!=0:
                    grid[node[0]+1][node[1]] = 2
                    que.append((node[0]+1,node[1]))
                if node[1]+1<m and grid[node[0]][node[1]+1]!=2 and grid[node[0]][node[1]+1]!=0:
                    grid[node[0]][node[1]+1] = 2
                    que.append((node[0],node[1]+1))
            if que:
                count += 1
        for i in range(n):
            if 1 in grid[i]:
                return -1
        return count
            
            
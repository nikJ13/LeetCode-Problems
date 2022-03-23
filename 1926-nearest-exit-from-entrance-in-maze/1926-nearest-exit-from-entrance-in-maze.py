class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = []
        queue.append((entrance[0], entrance[1]))
        vis = {}
        level = 0
        m = len(maze[0])
        n = len(maze)
        while len(queue)!= 0:
            for _ in range(len(queue)):
                ele = queue.pop(0)
                if ele in vis:
                    continue
                if (ele[0] == 0 or ele[1] == 0 or ele[0] == n-1 or ele[1] == m-1) and maze[ele[0]][ele[1]] == '.' and ele != (entrance[0], entrance[1]):
                    return level
                vis[ele] = 1
                dx = [0,0,1,-1]
                dy = [1,-1,0,0]
                for k in range(4):
                    cx = dx[k]+ele[0]
                    cy = dy[k]+ele[1]
                    if cx < 0 or cx >= n or cy < 0 or cy >= m:
                        continue
                    if maze[cx][cy] == '+':
                        continue
                    if (cx, cy) in vis:
                        continue
                    queue.append((cx, cy))
            level+=1
            
        return -1
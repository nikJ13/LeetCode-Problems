class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        n, m = len(maze), len(maze[0])
        visited = set()
        
        def dfs(x, y):
            # Already been here
            if (x, y) in visited:
                return False
            
            # Found destination
            if [x, y] == destination:
                return True
            
            visited.add((x, y))
            
            # Try all 4 directions
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                # Roll the ball until it hits a wall
                new_x, new_y = x, y
                while (0 <= new_x + dx < n and 
                       0 <= new_y + dy < m and 
                       maze[new_x + dx][new_y + dy] == 0):
                    new_x += dx
                    new_y += dy
                
                # Recursively check from where ball stopped
                if dfs(new_x, new_y):
                    return True
            
            return False
        
        return dfs(start[0], start[1])
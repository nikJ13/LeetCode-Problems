import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        [[1,2,2],[3,8,2],[5,3,5]]
        queue = [(2,1,0)]
        (1,0,1)
        """
        n,m = len(heights), len(heights[0])
        queue = [(0,0,0)]
        visited = set()
        while queue:
            curr_height_diff, x, y = heapq.heappop(queue)
            #print(curr_height_diff, x, y)
            if (x,y) in visited:
                continue
            if x==n-1 and y==m-1:
                return curr_height_diff
            visited.add((x,y))
            for delta_x, delta_y in [(0,1),(0,-1),(1,0),(-1,0)]:
                new_x, new_y = x + delta_x, y + delta_y
                if 0<=new_x<n and 0<=new_y<m:
                    new_height = heights[new_x][new_y]
                    new_height_diff = abs(new_height - heights[x][y])
                    heapq.heappush(queue, (max(new_height_diff,curr_height_diff), new_x, new_y))
        



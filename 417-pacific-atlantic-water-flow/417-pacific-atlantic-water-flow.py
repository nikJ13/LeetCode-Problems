class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atl = set(), set()
        def helper(x,y,prevHeight,visited):
            if(x<0 or y<0 or x==rows or y==cols or (x,y) in visited or heights[x][y]<prevHeight):
                return
            visited.add((x,y))
            helper(x+1,y,heights[x][y],visited)
            helper(x,y+1,heights[x][y],visited)
            helper(x-1,y,heights[x][y],visited)
            helper(x,y-1,heights[x][y],visited)
        ans = []
        for i in range(cols):    # first check if the water flows from the horizontal top and horizontal bottom into pacific and atlantic respectively
            helper(0,i,0,pacific)
            helper(rows-1,i,0,atl)
        for i in range(rows):  #check if the water flows from vertical left and right to the pacific and atlantic respectively
            helper(i,0,0,pacific)
            helper(i,cols-1,0,atl)
        # if there are points from where water flows into both the pacific and atlantic sets, then include them in the ans array
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atl:
                    ans.append([r,c])
        return ans
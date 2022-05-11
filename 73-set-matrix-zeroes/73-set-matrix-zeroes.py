class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        def helper(x,y,a,b):
            if x<0 or x>=m or y<0 or y>=n:
                return
            matrix[x][y] = 0
            helper(x+a,y+b,a,b)
        que = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    que.append((i,j))
        for node in que:
            helper(node[0]+1,node[1],1,0)
            helper(node[0],node[1]+1,0,1)
            helper(node[0]-1,node[1],-1,0)
            helper(node[0],node[1]-1,0,-1)
        
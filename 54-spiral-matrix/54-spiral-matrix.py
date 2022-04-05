class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = 0
        ans = []
        count = 0
        n_coll = 0
        n_colr = n-1
        n_rowt = 0
        n_rowb = m-1
        #print(matrix)
        while n_coll<=n_colr and n_rowt<=n_rowb:
            if count==0: # horizontal towards right traversal
                for i in range(n_coll,n_colr+1):
                    ans.append(matrix[n_rowt][i])
                count = 1
                n_rowt += 1
            elif count==1: # vertical down traversal
                for i in range(n_rowt,n_rowb+1):
                    ans.append(matrix[i][n_colr])
                count = 2
                n_colr -= 1
            elif count==2: # horizontal towards left traversal
                for i in range(n_colr,n_coll-1,-1):
                    ans.append(matrix[n_rowb][i])
                count = 3
                n_rowb -= 1
            elif count==3: # vertical towards top traversal
                for i in range(n_rowb,n_rowt-1,-1):
                    ans.append(matrix[i][n_coll])
                count = 0
                n_coll += 1
        return ans
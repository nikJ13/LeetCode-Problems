class Solution:
    def totalNQueens(self, n: int) -> int:
        cols_occupied = set()
        ans = 0
        posDiag = set()
        negDiag = set()
        
        def recurse(r):
            nonlocal ans
            if r==n:
                ans += 1
                return
            
            for i in range(n):
                if i not in cols_occupied and (r+i) not in posDiag and (r-i) not in negDiag:
                    cols_occupied.add(i)
                    posDiag.add(r+i)
                    negDiag.add(r-i)
                    recurse(r+1)
                    cols_occupied.remove(i)
                    posDiag.remove(r+i)
                    negDiag.remove(r-i)
        recurse(0)
        return ans
                    
                    
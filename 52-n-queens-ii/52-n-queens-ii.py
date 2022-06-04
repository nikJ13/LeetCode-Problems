class Solution:
    def totalNQueens(self, n: int) -> int:
        cols_occupied = set()
        ans = 0
        posDiag = set()
        negDiag = set()
        # in this problem, every row has one queen and every column also has one queen, but none are placed on eachother's diagonals, otherwise, they would cancel out, thus, we recurse through every row, checking if the column of that particular row already has a queen or not, by maintaining a set; simultaneously, we check for the positive (Slope) diagonals and negative (slope) diagnonals if they are present in the reapective set already [for a point (r,c), (r+c) is the same for a particular positive slope and (r-c) is the same for a particular negative slope]
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
                    
                    
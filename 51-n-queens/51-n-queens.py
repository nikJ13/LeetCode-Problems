class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols_occupied = set()
        posDiag = set()
        negDiag = set()
        board = [["."]*n for _ in range(n)]
        ans = []
        def recurse(r):
            if r==n:
                copy = ["".join(row) for row in board]
                ans.append(copy)
                return
            for i in range(n):
                if i not in cols_occupied and (r+i) not in posDiag and (r-i) not in negDiag:
                    board[r][i] = "Q"
                    cols_occupied.add(i)
                    posDiag.add(r+i)
                    negDiag.add(r-i)
                    recurse(r+1)
                    board[r][i] = "."
                    cols_occupied.remove(i)
                    posDiag.remove(r+i)
                    negDiag.remove(r-i)
        recurse(0)
        return ans
                    
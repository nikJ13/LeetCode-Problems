class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        idx = 0

        visited = set()
        m, n = len(board), len(board[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def recurse(i, j, idx):
            if idx==len(word):
                # print("reached")
                return True
            temp = False
            # print(idx)
            for x,y in directions:
                new_x = i+x
                new_y = j+y
                # print("new_x", new_x)
                # print("new_y", new_y)
                if (new_x>=0 and new_x<m) and (new_y>=0 and new_y<n):
                    # print("inside")
                    if (new_x, new_y) not in visited and board[new_x][new_y]==word[idx]:
                        visited.add((new_x, new_y))
                        temp = recurse(new_x, new_y, idx+1)
                        visited.remove((new_x, new_y))
                        if temp==True:
                            return True
            # print("for",word[idx])
            # print("temp received", temp)
            return False
        
        ans = None
        for p in range(m):
            for q in range(n):
                if word[idx]==board[p][q]:
                    visited.add((p,q))
                    ans = recurse(p, q, 1)
                    visited.remove((p,q))
                    if ans==True:
                        return True
        return False



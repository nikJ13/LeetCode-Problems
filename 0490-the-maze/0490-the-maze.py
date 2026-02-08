class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        """
        Problem: Prove whether the ball can reach the destination
        Solution:
        We should execute a recursive function in such a way that if the ball reaches some wall or end of the maze,
        then it will call the recursive function in all directions except the previous direction
        Hence, it should pass the previous direction it is going in
        If no wall encountered at the current recursion, then call another recursive function in the same direction
        as the previous direction with +1 counter to change the coordinate of the ball in the maze
        we need to make sure that the ball is not reusing the same direction for a particular block in the maze
        we basically check if the next block in the same prev dir is a wall or not
        if it is a wall (out of bounds),
            then check for all other directions apart from prev and if that new direction is not a wall or not already visited
                if so then mark the new block as visited and traverse to it
                when coming back with the result, mark it unvisited so that other paths can reuse that block
        we need to keep track of unique directions at every position, instead of marking it visited
        """
        n, m = len(maze), len(maze[0])
        directions = {"up":(-1,0),"down":(1,0),"left":(0,-1),"right":(0,1)}
        maze_directions = [[set() for _ in range(m)] for _ in range(n)]
        def helper(curr_x, curr_y, prev_dir):
            xchange, ychange = directions[prev_dir]
            new_x, new_y = curr_x + xchange, curr_y + ychange
            if new_x<0 or new_x>=n or new_y<0 or new_y>=m: # checking if the next move in the same prev dir will be a wall
                # call for recursion in other directions except prev_dir
                if [curr_x, curr_y] == destination: # we need to check if we can stop the ball
                    return True
                for dirs in directions:
                    if dirs!=prev_dir:
                        xchange, ychange = directions[dirs]
                        new_x, new_y = curr_x + xchange, curr_y + ychange
                        # keep a check of which directions are valid
                        if (new_x>=0 and new_x<n) and (new_y>=0 and new_y<m):
                            if maze[new_x][new_y]!=1 and dirs not in maze_directions[curr_x][curr_y]:
                                maze_directions[curr_x][curr_y].add(dirs)
                                res = helper(new_x, new_y, dirs)
                                if res:
                                    return True
            elif maze[new_x][new_y]==1: # if the next block is a wall
                # call for recursion in other directions except prev_dir
                if [curr_x, curr_y] == destination: # we need to check if we can stop the ball
                    return True
                for dirs in directions:
                    if dirs!=prev_dir:
                        xchange, ychange = directions[dirs]
                        new_x, new_y = curr_x + xchange, curr_y + ychange
                        if (new_x>=0 and new_x<n) and (new_y>=0 and new_y<m):
                            if maze[new_x][new_y]!=1 and dirs not in maze_directions[curr_x][curr_y]:
                                maze_directions[curr_x][curr_y].add(dirs)
                                res = helper(new_x, new_y, dirs)
                                if res:
                                    return True
            else:
                maze_directions[curr_x][curr_y].add(prev_dir)
                res = helper(new_x, new_y, prev_dir)
                if res:
                    return True
            return False

        """
        [[0,0,1,0,0],
         [0,0,0,0,0],
         [0,0,0,1,0],
         [1,1,0,1,1],
         [0,0,0,0,0]]

        """

        x, y = start[0], start[1]
        # we need to check in which directions can one go from the start
        for dirs in directions:
            xchange, ychange = directions[dirs]
            new_x, new_y = x + xchange, y + ychange
            if (new_x>=0 and new_x<n) and (new_y>=0 and new_y<m):
                if maze[new_x][new_y]!=1 and dirs not in maze_directions[x][y]:
                    maze_directions[x][y].add(dirs)
                    res = helper(new_x, new_y, dirs)
                    if res:
                        return True
        return False
        
            
            


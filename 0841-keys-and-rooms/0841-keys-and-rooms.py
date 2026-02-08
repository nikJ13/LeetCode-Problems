class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(curr_room):
            visited.add(curr_room)
            if len(rooms[curr_room])==0:
                return
            for keys in rooms[curr_room]:
                if keys not in visited:
                    dfs(keys)
        
        dfs(0)
        if len(visited)==len(rooms):
            return True
        else:
            return False
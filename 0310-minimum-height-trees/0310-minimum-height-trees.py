class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(n)}
        for edge in edges:
            v1, v2 = edge[0], edge[1]
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        def traverse(node):
            if node in visited:
                return 0
            visited.add(node)
            if not adj[node]:
                return 1
            max_h = 0
            for neighs in adj[node]:
                h = traverse(neighs)
                max_h = max(h, max_h)
            return max_h + 1
        ans = []
        ans_heights = []
        min_h = float("inf")
        for roots in adj:
            visited = set()
            height = traverse(roots)
            min_h = min(height, min_h)
            ans_heights.append((roots, height))
        
        for tups in ans_heights:
            if tups[1]==min_h:
                ans.append(tups[0])
        return ans
        
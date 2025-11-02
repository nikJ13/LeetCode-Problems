class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        adj = {}
        for key, val in replacements:
            adj[key] = list(val)
        ans = ""
        def dfs(ch):
            temp = ""
            for neighs in adj[ch]:
                if neighs=="%":
                    continue
                if neighs in adj:
                    temp += dfs(neighs)
                else:
                    temp += neighs
            return temp
        for ch in text:
            if ch=="%":
                continue
            if ch in adj:
                ans += dfs(ch)
            else:
                ans += ch
        return ans
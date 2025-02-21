class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for s in strs:
            ana[''.join(sorted(s))].append(s)
        ans = [j for j in ana.values()]
        return ans
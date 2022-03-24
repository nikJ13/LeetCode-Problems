class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def recurse(index,temp):
            if index==len(graph)-1:
                ans.append(temp[:])
                return
            if len(graph[index])==0:
                return
            for i in range(len(graph[index])):
                temp.append(graph[index][i])
                recurse(graph[index][i],temp)
                temp.pop()
        recurse(0,[0])
        return ans
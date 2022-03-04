class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def recurse(temp,k,ele):
            #nonlocal ans
            if k==0:
                #print("here",temp)
                ans.append(temp[:])
                #print(ans)
                return
            #print(temp)
            for i in range(ele+1,n-k+2):
                #print("start",ans)
                temp.append(i)
                #print(temp)
                recurse(temp,k-1,i)
                #print("there",ans)
                temp.pop()
        ans = []
        for j in range(1,n-k+2):
            recurse([j],k-1,j)
        return ans
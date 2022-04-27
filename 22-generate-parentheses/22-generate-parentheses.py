class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def helper(nOpen,nClose,temp,stack):
            #print(stack)
            if nOpen==0 and nClose==0:
                ans.append(temp)
                return
            if nOpen!=0:
                helper(nOpen-1,nClose,temp+"(",stack+1)
            if nClose!=0 and stack!=0:
                helper(nOpen,nClose-1,temp+")",stack-1)

        helper(n,n,"",0)
        return ans
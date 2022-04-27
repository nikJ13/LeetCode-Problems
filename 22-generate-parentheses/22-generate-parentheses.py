class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        # Here, nOpen and nClose are the number of open and closed brackets respectively. So at each position in the answer string, there are two options, either insert opening or closing brackets, and this is possible only if the number of those brackets left are not zero. Also, in order to make valid combinations, the stack counter should be there, so whenever there is a push, then increment its value, and if there is a pop, then check if the stack is zero (empty of not), if not so, then there is still scope to form valid string, otherwise it reverses back to the previous recursion
        def helper(nOpen,nClose,temp,stack):
            if nOpen==0 and nClose==0:
                ans.append(temp)
                return
            if nOpen!=0:
                helper(nOpen-1,nClose,temp+"(",stack+1)
            if nClose!=0 and stack!=0:
                helper(nOpen,nClose-1,temp+")",stack-1)

        helper(n,n,"",0)
        return ans
class Solution:
    def checkValidString(self, s: str) -> bool:
        left,right = 0,0
        for i in s:
            if i=="(" or i=="*":
                left += 1
            else:
                left -= 1
            if left<0:
                return False # We know we have unbalanced parenthesis
        if left==0: #We can already check if parenthesis are valid
            return True
        for i in range(len(s)-1,-1,-1):
            if s[i]==")" or s[i]=="*":
                right += 1
            else:
                right -= 1
            if right<0:
                return False # We know we have unbalanced parenthesis
            
        # Here we know we have never been unbalanced parsing from left to right e.g. ')('
        # We've also already substituted '*' either by '(' or by ')'
        # So we only have 3 possible scenarios here:
        # 1. We had the same amount of '(' and ')'
        # 2. We had more '(' then ')' but enough '*' to substitute
        # 3. We had more ')' then '(' but enough '*' to substitute
        return True
                
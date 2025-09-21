class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l = []
        operatorMap = { 
            "*": lambda x, y: x*y, 
            "+": lambda x, y: x+y, 
            "-": lambda x, y: x-y, 
            "/": lambda x, y: int(x/y)
        }
        
        for token in tokens:
            
            if token not in operatorMap:
                l.append(int(token))
            
            # if operator, pop 2 numbers and perform operator
            else:
                num2, num1 = l.pop(), l.pop()
                result = operatorMap[token](num1, num2)
                l.append(result)  
        
        return l.pop()
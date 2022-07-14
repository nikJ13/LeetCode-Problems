class Solution:
    def isHappy(self, n: int) -> bool:
        
        def calculate(number):
            res = 0
            while number>0:
                res += (number%10)**2
                number = number//10
            return res
                
        set1 = set()
        
        while n!=1:
            n = calculate(n)
            if n in set1:
                return False
            set1.add(n)
        return True
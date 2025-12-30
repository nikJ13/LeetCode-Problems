class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n, m = len(num1), len(num2)
        if n<m:
            left = m - n
            num1 = "0"*left + num1
        elif n>m:
            left = n - m
            num2 = "0"*left + num2
        l = len(num1)
        carry = 0
        ans = ""
        for i in range(l-1,-1,-1):
            summation = int(num1[i]) + int(num2[i]) + carry
            carry = summation // 10
            final_sum = summation % 10
            ans = str(final_sum) + ans
        if carry==1:
            ans = "1" + ans
        return ans
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0],0)]
        ans = [0]*len(temperatures)
        start = 1
        while start<len(temperatures):
            temp = temperatures[start]
            if temp > stack[-1][0]:
                while len(stack) and temp > stack[-1][0]:
                    t, i = stack.pop()
                    ans[i] = start - i
            stack.append((temp, start))
            start += 1
        return ans
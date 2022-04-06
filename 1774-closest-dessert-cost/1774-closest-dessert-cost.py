class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        costs = set()
        diff = 100000
        ans = 100000
        def helper(number,index):
            nonlocal diff
            if index>=len(toppingCosts):
                costs.add(number)
                diff = min(diff,abs(number-target))
                return
            helper(number,index+1)
            helper(number+toppingCosts[index],index+1)
            helper(number+(toppingCosts[index]*2),index+1)
            
        for i in range(len(baseCosts)):
            helper(baseCosts[i],0)
        for j in costs:
            if abs(target-j)==diff:
                ans = min(ans,j)
        return ans
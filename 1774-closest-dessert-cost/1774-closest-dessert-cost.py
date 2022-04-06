class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        #when the question says closest to the target value, then the sum of the base + toppings can also be greater than the target value and be closer to it.
        costs = set()
        diff = 100000
        ans = 100000
        def helper(number,index):
            nonlocal diff
            if index>=len(toppingCosts):
                costs.add(number)
                diff = min(diff,abs(number-target))
                return
            # there are three options for each step, either don't add the particular topping, add one quantity of that topping or add two quantities of that topping; in all the three cases the index should be incremented to the next topping
            helper(number,index+1)
            helper(number+toppingCosts[index],index+1)
            helper(number+(toppingCosts[index]*2),index+1)
            
        for i in range(len(baseCosts)):
            helper(baseCosts[i],0)
        # to find the lower number that has the same difference from the target than another higher number
        for j in costs:
            if abs(target-j)==diff:
                ans = min(ans,j)
        return ans
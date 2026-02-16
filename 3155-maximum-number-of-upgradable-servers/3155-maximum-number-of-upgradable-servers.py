class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        """
        Problem: Need to find the maximum number of servers that can be upgraded
        Solution:
        Given I have the total money t. 
        money for selling a server =>x
        money for upgrading a server => y
        number of servers => s

        max(M*i)

        where M = t + qx = multiple of y
        and i = s - q

        this has to be divide into subproblems
        can money t be enough?
        do we have to sell to get more money?

        [(money,count)]
        [(total_money,total_servers),(total_money+sell,total_servers-1)]
        [(8,4),(12,3)] => at each level we check if we can upgrade or not; if we can then no need to traverse further down the tree, else we have to

        count = [4,3], upgrade = [3,5], sell = [4,2], money = [8,9]
        helper(8,4,0)

        helper(4+8,4-1,0) => helper(12,3,0)

        helper(4+4+8,4-2,0)

        count c
        upgrade u
        sell s
        money m

        assuming we sell (c-k) servers

        k*u <= s*(c-k) + m
        we need to find k servers value

        ku <= sc - sk + m
        k <= (sc + m)/(u+s)

        """
        ans = []
        for i in range(len(count)):
            k = (sell[i]*count[i] + money[i])//(upgrade[i] + sell[i])
            ans.append(min(k,count[i]))
        return ans

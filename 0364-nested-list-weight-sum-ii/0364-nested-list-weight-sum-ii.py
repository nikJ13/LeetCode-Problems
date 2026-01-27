# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        """
        Problem: get the weight of the whole nestedlist
        
        [[1,1],2,[1,1]]
        [NestedInteger,NestedInteger,NestedInteger]
        
        [2 , 1 , 2] => max depth = 2
        global_list = 
        w1 = 2 - 2 + 1
        w2 = 2 - 2 + 1
        w1 + w2 = 4 - 4 + 2
        [NestedInteger(max(depths amongst its children)+1,[an array of all the depths from this object]),NestedInteger(1),NestedInteger(max(depths amongst its children)+1,[an array of all the depths from this object])] => ifInteger => False => getList => [NestedInteger(1),NestedInteger(1)] => iterate and check ifInteger => True (1)
        [[1,1],2,[1,1]]
        
        
        a[i]*weight
        a[i]*(maxdepth - depth + 1)
        a[i]*max_depth - a[i]*depth + a[i]
        Sum(a[i]*(maxdepth + 1) - a[i]*depth)
        (maxdepth+1)Sum(a[i]) - Sum(a[i]*depth)
        
        """
        
        def helper(list_obj,curr_depth):
            sum_prev_lvl, weight_sum_prev_lvl = 0, 0
            sum_lvl, weight_sum_lvl = 0, 0
            curr_max_depth = float("-inf")
            for obj in list_obj:
                if obj.isInteger():
                    # print("here")
                    sum_lvl += obj.getInteger()
                    weight_sum_lvl += obj.getInteger()*curr_depth
                    curr_max_depth = max(curr_depth,curr_max_depth)
                else:
                    # print("there")
                    nested_list = obj.getList()
                    sum_prev_lvl, weight_sum_prev_lvl, max_depth = helper(nested_list,curr_depth+1)
                    sum_lvl += sum_prev_lvl
                    weight_sum_lvl += weight_sum_prev_lvl
                    curr_max_depth = max(curr_max_depth, max_depth)
                    # keep track of the depths here
            # print(sum_lvl)
            # print(weight_sum_lvl)
            # print(curr_max_depth)
            return sum_lvl, weight_sum_lvl, curr_max_depth
        
        sum_elements, weight_sum, final_max_depth = helper(nestedList,1)
        # print("final",sum_elements, weight_sum, final_max_depth)
        return (final_max_depth+1)*sum_elements - weight_sum
                
                 
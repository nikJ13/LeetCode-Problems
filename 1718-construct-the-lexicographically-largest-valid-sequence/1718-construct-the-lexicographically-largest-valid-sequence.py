class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        length = ((n-1)*2) + 1 # Based on the given condition, this is the length of the answer array
        visit = set() # visited nodes will be stored here
        ans = [0]*length
        def helper(index,visit):
            if len(visit)==n or index>=length: # if the visited set has all the nodes (since no duplicates are allowed in the set) or the current index is greater than the length of the answer array
                return True
            if ans[index]!=0: # if the current index in the answer array already has another number then move on to the next index
                return helper(index+1,visit)
            for i in range(n,0,-1): # iterating from 'n' to '1' backwards, since the greater lexographical number will have greater elements in the front (given that it satisfies the conditions)
                if i in visit: # if the current number is already visited then skip it
                    continue
                if i!=1 and i+index>=length: # if the current number is greater than 1, such that the current index+current number gives an index which is out of bounds, then skip the current number
                    continue
                if i!=1 and ans[index+i]!=0: # if the current number is greater than 1 and the ans number present at the current index+ current number position already has another number, then skip the current number
                    continue
                visit.add(i) # the current number is visited
                ans[index] = i # the answer array is updated accordingly
                if i!=1: # if the current number is not equal to one, then update the (index+i)th position
                    ans[index+i] = i 
                if helper(index+1,visit): # move onto the next index
                    return True #stop once we find the first working sequence
                else:
                    if i!=1: 
                        ans[index+i] = 0 # reset the ans values if the condition is not satisfied
                    ans[index] = 0 # reset the ans values if the condition is not satisfied
                visit.remove(i) # since the current number does not work, it is removed from the visited set
            return False # since, none of the combinations work return the appropriate result
        
        helper(0,visit) # start from the starting index of the answer array 
        return ans
        
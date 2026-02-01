# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        """
        Problem: Need to find ther celebrity
        Solution: 
        1. calculate the outdegrees of each element
            need to make the least amount of calls to the api
            I was thinking of iterating for every pair
            (a,b,c,d)
            (n-1)! number of api calls
            What if we can perform a binary search where we compare the lower and the mid and the higher and the mid element
            we are trying to frame mid to be the celebrity
            0->2;2->1;1->0
            (0,1,2)


            (2,0)

            we check if a knows b; if yes, then b is a suspect; shift upper bound to mid
                                   if not, then shift lower bound to mid + 1
            we check if c knows b; if yes, then b again is a suspect
                                   if not, then shift the lower bound to mid+1
            
            we check if a knows b and d knows b;
                if yes, then b is a suspect; shift upper bound to mid
            else:
                if a does not know b:
                    shift the upperbound to mid
                if d does not know b:
                    shift lower bound to mid + 1
        2. whoever's outdegree is 0, that is the celebrity

        New approach:
        We compare every node pair and if we find one node does not know the other, then this node stays
        0->1; 1->0
        (0,1)
        """
        candidate = 0
        for i in range(n):
            if candidate!=i:
                if knows(candidate,i): # 1 knows 0
                    candidate = i
        for i in range(n):
            if candidate!=i:
                if not knows(i,candidate) or (knows(i,candidate) and knows(candidate,i)): # if i does not know the candidate # 0 knows 1
                    return -1
        return candidate


        
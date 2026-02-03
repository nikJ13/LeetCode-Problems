class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        """
        Problem: Get an array such that each element will be like:
            [arr[0],arr[0]^arr[1],.....]
        arr = []
        for number in element at index 1 to end of pref:
            pref[i] = xor(pref[i],pref[i-1])
        
        
        pref xor ans = pref_curr
        
        
        5 ^ 7 = 2
        5 ^ 2 = 7
        
        
        
        Store all the prefix xors
        
        101
        111
        _____
        010
        
        101
        101
        ____
        000
        
        
        101
        010
        ____
        111
        
        0 xor 0 = 0
        1 xor 0 = 1
        0 xor 1 = 1
        1 xor 1 = 0
        """
        """
        pref = [5,2,0,3,1]
        ans =  [5,7,2,3,2]
        
        previous pref element ^ current pref element
        001
        011
        ___
        010
        """
        ans = [pref[0]]
        for i in range(1,len(pref)):
            ans.append(pref[i-1]^pref[i])
        return ans
        
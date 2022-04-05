class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        length = ((n-1)*2) + 1
        visit = set()
        ans = [0]*length
        def helper(index,visit):
            if len(visit)==n or index>=length:
                return True
            if ans[index]!=0:
                return helper(index+1,visit)
            for i in range(n,0,-1):
                if i in visit:
                    continue
                if i!=1 and i+index>=length:
                    continue
                if i!=1 and ans[index+i]!=0:
                    continue
                visit.add(i)
                ans[index] = i
                if i!=1:
                    ans[index+i] = i
                if helper(index+1,visit):
                    return True
                else:
                    if i!=1:
                        ans[index+i] = 0
                    ans[index] = 0
                visit.remove(i)
            return False
        helper(0,visit)
        return ans
        
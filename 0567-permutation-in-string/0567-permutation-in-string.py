class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        alpha, temp = [0]*26, [0]*26
        for i in s1:
            alpha[ord(i)-97] += 1
        start, end = 0, len(s1)-1
        for i in range(len(s1)):
            temp[ord(s2[i])-97] += 1
        while end<=len(s2):
            if alpha==temp:
                return True
            temp[ord(s2[start])-97] -= 1
            start += 1
            end += 1
            if end==len(s2):
                break
            temp[ord(s2[end])-97] += 1
        return False

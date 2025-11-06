class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        ans = []
        m, n = len(matrix), len(matrix[0])
        while True:
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1
            if top>=bottom:
                return ans
            for j in range(top, bottom):
                ans.append(matrix[j][right-1])
            right -= 1
            if left>=right:
                return ans
            for k in range(right-1, left-1, -1):
                ans.append(matrix[bottom-1][k])
            bottom -= 1
            if top>=bottom:
                return ans
            for g in range(bottom-1, top-1, -1):
                ans.append(matrix[g][left])
            left += 1
            if left>=right:
                return ans
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        for j in range(n):
            res.append(matrix[0][j])
        if m > 1:
            for i in range(1, m):
                res.append(matrix[i][n-1])
        if m > 1 and n > 1: 
            for j in range(n-2, -1, -1):
                res.append(matrix[m-1][j])
        if m > 2 and n > 1:
            for i in range(m-2, 0, -1):
                res.append(matrix[i][0])
        inner = [row[1:n-1] for row in matrix[1:m-1]]
        return res + self.spiralOrder(inner)


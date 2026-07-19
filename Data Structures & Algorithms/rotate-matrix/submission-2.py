class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])

        l, r = 0, n-1
        while l<r:
            row = matrix[l]
            matrix[l] = matrix[r]
            matrix[r] = row
            l +=1
            r -=1
        
        for i in range(n):
            for j in range(i+1, n):
                pointer = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = pointer

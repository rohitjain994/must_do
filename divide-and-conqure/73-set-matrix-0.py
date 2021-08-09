class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r,c = len(matrix),len(matrix[0])
        row,col = set(),set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j] ==0:
                    row.add(i)
                    col.add(j)
        for i in range(r):
            for j in range(c):
                if i in row or j in col:
                    matrix[i][j] = 0
        
        
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

# You must do it in place.
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        m, n = len(matrix[0]), len(matrix)
        l, r = 0, m*n - 1
        while l < r:
            mid = (l + r)//2
            if matrix[mid//m][mid%m] == target:
                return True
            elif matrix[mid//m][mid%m] < target:
                l = mid + 1
            else:
                r = mid
        return matrix[l//m][l%m] == target

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
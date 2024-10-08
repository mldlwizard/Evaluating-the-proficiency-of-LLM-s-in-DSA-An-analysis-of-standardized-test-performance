from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        row, col = rows - 1, 0
        
        while row >= 0 and col < cols:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col += 1
            else:
                row -= 1
                
        return False
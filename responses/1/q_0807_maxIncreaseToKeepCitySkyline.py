from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        max_row = [max(row) for row in grid]
        max_col = [max(grid[r][c] for r in range(n)) for c in range(n)]

        total_increase = 0
        for r in range(n):
            for c in range(n):
                total_increase += min(max_row[r], max_col[c]) - grid[r][c]

        return total_increase
class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_not_under_attack(row, col, queens):
            return all(row != r and col != c and row - col != r - c and row + col != r + c for r, c in queens)

        def backtrack(row, queens):
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if is_not_under_attack(row, col, queens):
                    count += backtrack(row + 1, queens + [(row, col)])
            return count

        return backtrack(0, [])
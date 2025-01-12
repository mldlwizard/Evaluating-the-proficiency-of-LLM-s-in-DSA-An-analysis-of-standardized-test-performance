from typing import List

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        memo = [[[0] * n for _ in range(n)] for _ in range(n)]

        def dp(left, right, k):
            if left > right:
                return 0

            if memo[left][right][k] != 0:
                return memo[left][right][k]

            while right > left and boxes[right] == boxes[right - 1]:
                right -= 1
                k += 1

            memo[left][right][k] = dp(left, right - 1, 0) + (k + 1) * (k + 1)

            for i in range(left, right):
                if boxes[i] == boxes[right]:
                    memo[left][right][k] = max(memo[left][right][k], dp(left, i, k + 1) + dp(i + 1, right - 1, 0))

            return memo[left][right][k]

        return dp(0, n - 1, 0)

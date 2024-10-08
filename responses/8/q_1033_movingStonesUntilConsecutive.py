from typing import List

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        stones = [a, b, c]
        stones.sort()
        
        if stones[2] - stones[0] == 2:
            return [0, 0]
        
        min_moves = 1 if stones[1] - stones[0] > 2 or stones[2] - stones[1] > 2 else 2
        max_moves = stones[2] - stones[1] - 1 + stones[1] - stones[0] - 1

        return [min_moves, max_moves]
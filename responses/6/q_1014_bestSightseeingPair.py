from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        curr_max = values[0] + 0
        
        for j in range(1, len(values)):
            max_score = max(max_score, curr_max + values[j] - j)
            curr_max = max(curr_max, values[j] + j)
        
        return max_score
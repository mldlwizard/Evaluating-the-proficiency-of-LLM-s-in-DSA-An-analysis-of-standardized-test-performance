from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        arrow_pos = points[0][1]
        arrows = 1

        for start, end in points:
            if start > arrow_pos:
                arrow_pos = end
                arrows += 1

        return arrows
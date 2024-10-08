from typing import List

class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        def dfs(image, r, c, color, newColor):
            if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]) or image[r][c] != color:
                return
            if image[r][c] == color:
                image[r][c] = newColor
                dfs(image, r+1, c, color, newColor)
                dfs(image, r-1, c, color, newColor)
                dfs(image, r, c+1, color, newColor)
                dfs(image, r, c-1, color, newColor)

        if image[sr][sc] != newColor:
            dfs(image, sr, sc, image[sr][sc], newColor)
        
        return image
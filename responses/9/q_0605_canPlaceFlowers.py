from typing import List

class Solution:
    
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        flowerbed.append(0)
        flowerbed.insert(0, 0)
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count += 1
        return count >= n

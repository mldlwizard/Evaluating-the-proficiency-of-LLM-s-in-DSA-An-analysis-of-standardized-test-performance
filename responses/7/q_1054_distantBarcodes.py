from collections import Counter
from heapq import heappop, heappush

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        heap = [(-freq, num) for num, freq in counter.items()]
        heapq.heapify(heap)
        
        result = []
        while len(heap) > 1:
            freq1, num1 = heapq.heappop(heap)
            freq2, num2 = heapq.heappop(heap)
            
            result.extend([num1, num2])
            
            if freq1 + 1 < 0:
                heapq.heappush(heap, (freq1 + 1, num1))
            if freq2 + 1 < 0:
                heapq.heappush(heap, (freq2 + 1, num2))
        
        if heap:
            freq, num = heapq.heappop(heap)
            result.append(num)
            
        return result
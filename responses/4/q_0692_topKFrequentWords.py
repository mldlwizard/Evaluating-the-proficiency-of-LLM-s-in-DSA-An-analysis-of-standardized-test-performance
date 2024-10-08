from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = Counter(words)
        heap = [(-freq, word) for word, freq in word_counts.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
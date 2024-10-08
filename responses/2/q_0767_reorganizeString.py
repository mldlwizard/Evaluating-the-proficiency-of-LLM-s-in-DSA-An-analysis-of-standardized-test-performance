class Solution:
    def reorganizeString(self, s: str) -> str:
        import heapq
        from collections import Counter

        counter = Counter(s)
        max_heap = [(-value, key) for key, value in counter.items()]
        heapq.heapify(max_heap)

        result = []
        prev_count, prev_char = 0, ''

        while max_heap:
            count, char = heapq.heappop(max_heap)

            result.append(char)
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))

            count += 1
            prev_count, prev_char = count, char

        result = ''.join(result)

        return result if len(result) == len(s) else ""
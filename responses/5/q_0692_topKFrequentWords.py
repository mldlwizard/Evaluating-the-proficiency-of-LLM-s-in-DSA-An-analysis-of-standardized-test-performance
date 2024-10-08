from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = Counter(words)
        unique_words = list(word_count.keys())
        
        unique_words.sort(key=lambda word: (-word_count[word], word))
        
        return unique_words[:k]
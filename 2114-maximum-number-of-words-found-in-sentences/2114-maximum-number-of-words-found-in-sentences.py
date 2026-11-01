class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_words = 0
        for s in sentences:
            count = len(s.split())
            max_words = max(max_words, count)
        return max_words
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_word = words[::-1]
        result = " ".join(reversed_word)
        return result
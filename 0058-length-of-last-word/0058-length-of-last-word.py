# Method 1:
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()
        return len(word[-1])

# Method 2:
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         i = len(s) - 1
#         length =  0
#         while i>=0 and s[i] == ' ':
#             i -= 1
#         while i >=0 and s[i] != ' ':
#             length +=1
#             i -= 1
#         return length 
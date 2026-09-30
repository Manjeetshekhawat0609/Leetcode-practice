# Method 1
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

# Method 2
# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         return self.fib(n-1) + self.fib(n-2)

# Method 3
# class Solution:
#     def fib(self, n: int) -> int:
#         return n if n <= 1 else self.fib(n - 1) + self.fib(n - 2)
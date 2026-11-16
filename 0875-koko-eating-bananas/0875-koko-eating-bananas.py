class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            hours = sum((p + mid - 1) // mid for p in piles)
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        return left 
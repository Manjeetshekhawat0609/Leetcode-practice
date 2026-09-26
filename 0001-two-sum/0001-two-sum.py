class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            needed = target - num
            if needed in seen:
                return [seen[needed], i]
            seen[num] = i

# Method 2:
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         seen = {}
#         for i, num in enumerate(nums):
#             needed = target - num
#             if needed in seen:
#                 return [seen[needed], i]
#             seen[num] = i
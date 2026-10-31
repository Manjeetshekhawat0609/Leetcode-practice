# Method 1
# class Solution:
#     def maximumWealth(self, accounts: list[list[int]]) -> int:
#         return max(sum(customer) for customer in accounts)

# Method 2
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            current_wealth = sum(customer)
            max_wealth = max(max_wealth, current_wealth)
        return max_wealth
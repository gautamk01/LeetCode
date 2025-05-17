class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        total = prices[0] + prices[1]
        if (total <= money):
            return money-total
        else:
            return money

# 🔹 Problem: [2706. Buy Two Chocolates]
# 🧠 Highlight: Buy exactly 2 chocolates such that:

# Their combined cost is minimized.
# You don’t go into debt (remaining money ≥ 0).

# 💡 My Approach:

# 1. Sort the prices list.
# 2.Pick the two cheapest chocolates (first two elements).
# 3.Check if their sum is within the available money:
# 4.If yes, return money - total.
# 5.if not, return money (can't buy both without debt).

# 📌 Key Logic: Greedy approach – always choose the two least expensive options to minimize cost and preserve leftover money.

# ⏱ Time Complexity: O(n log n) – for sorting.
# 📦 Space Complexity: O(1) – in-place operations only.

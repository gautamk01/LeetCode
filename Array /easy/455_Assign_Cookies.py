#  Problem: [455. Assign Cookies]
#  Highlight: Each child has a greed factor, and each cookie has a size. A cookie can satisfy a child only if size ≥ greed. Maximize the number of content children.

# 💡 My Approach:

# Sort both g (greed factors) and s (cookie sizes).
# Use two pointers:
#   r to iterate children
#   l to iterate cookies
# While cookies and children are available:
#   If the current cookie satisfies the current child, count it and move to the next child.
#   Move to the next cookie either way.

# 📌 Key Logic: Greedy two-pointer technique — always try to satisfy the least greedy child first with the smallest available cookie.

# ⏱ Time Complexity: O(n log n + m log m ) – For sorting both arrays.
# 📦 Space Complexity: O(1) – Constant extra space used.

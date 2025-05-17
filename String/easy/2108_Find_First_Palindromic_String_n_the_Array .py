class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            rev = i[::-1]
            if (i == rev):
                return i
        return ""

# 🔹 Problem: [2108. Find First Palindromic String in the Array]
# 🧠 Highlight: Return the first word in the list that reads the same forward and backward.

# 💡 My Approach:

# Loop through each word in the list.
# For each word, use slicing [::-1] to reverse it.
# If the reversed word equals the original, return it immediately.
# If none match, return an empty string.

# Key Logic: Leverage Python’s clean slicing to check for palindromes efficiently.

# ⏱ Time Complexity: O(n * k) –
# Where n = number of words, k = average word length.

# Space Complexity: O(1) – No extra space used besides variables.

class Solution:
    def makeFancyString(self, s: str) -> str:
        prev = s[0]
        count = 1
        ans = s[0]
        for i in range(1, len(s)):
            if (prev == s[i]):
                count += 1
            else:
                prev = s[i]
                count = 1
            if (count < 3):
                ans += s[i]
        return ans


# 🔹 Problem: [1957. Delete Characters to Make Fancy String]
# 🧠 Highlight: A fancy string must not have three consecutive repeating characters.

# 💡 My Approach:

# 1. Start with the first character as prev, and set its count to 1.
# 2. Loop through the string from the second character onward.
# 3. If the current character matches prev, increment the count.
# 4. If it's different, reset prev and count = 1.
# 5.Append the current character to the result only if count < 3.

# ⏱ Time Complexity: O(n) – Single pass through the string.
# 📦 Space Complexity: O(n) – For the result string.

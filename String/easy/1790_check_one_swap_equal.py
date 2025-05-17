class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if (len(s1) != len(s2)):
            return False
        else:
            if (s1 == s2):
                return True
            else:
                v1 = list(s1)
                v2 = list(s2)
                res = []
                count = 0
                for i in range(len(v1)):
                    if (v1[i] != v2[i]):
                        count += 1
                        res.append(i)

                if (count == 2):
                    print(count, res)
                    temp = v1[res[0]]
                    v1[res[0]] = v1[res[1]]
                    v1[res[1]] = temp
                    final_v1 = ''.join(v1)
                    final_v2 = ''.join(v2)
                    if (final_v2 == final_v1):
                        return True
                    else:
                        return False
                else:
                    return False

# 🔹 Problem: [1790. Check if One String Swap Can Make Strings Equal]
# 🧠 Highlight: We’re allowed to swap only one pair of characters in s1 to match s2.

# 💡 My Approach:

# First, check if lengths of s1 and s2 are equal.
# If both strings are already equal, return True.
# Otherwise, find all indices where characters differ.
# If there are exactly 2 mismatches, try swapping those two characters in s1.
# If post-swap, s1 == s2, return True; else return False.
# 📌 Key Logic: Only two characters can differ — and only one swap is allowed.

# ⏱ Time Complexity: O(n) – We only loop through the string once.
# 📦 Space Complexity: O(1) – Fixed space (apart from minor list use).

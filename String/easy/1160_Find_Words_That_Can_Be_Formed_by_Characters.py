
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        re = {}
        for k in chars:
            if (re.get(k)):
                re[k] += 1
            else:
                re[k] = 1
        final = 0
        for i in words:
            demi = re.copy()
            success = True
            count = 0
            for j in i:
                if (demi.get(j)):
                    count += 1
                    demi[j] -= 1
                else:
                    success = False
                    break
            if (success):
                final += count
        return final


# 💡My Approach:

# First, build a dictionary (re) to store the frequency of each character in chars.

# For each word in words:
#   Make a copy of the original character dictionary.
#   Check if the word can be formed with the available characters.
#   If successful, add the word's length to the final count.

# Key Logic: Use a frequency map and copy it for each word to validate availability without mutating the original.

# ⏱ Time Complexity: O(m + n * k)
# Where:
# m = length of chars
# n = number of words
# k = average word length

# Space Complexity: O(1) – Since character set size is limited (lowercase English letters).

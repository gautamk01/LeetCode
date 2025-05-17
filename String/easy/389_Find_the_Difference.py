class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = {}
        for i in t:
            if (res.get(i)):
                res[i] += 1
            else:
                res[i] = 1
        for i in s:
            if (res.get(i)):
                res[i] -= 1
                if (res[i] == 0):
                    del res[i]
        return next(iter(res))


#  Problem: [389. Find the Difference]
#  Highlight: Given two strings s and t where t has one extra letter, find the added character.

#  My Approach:

#  1. Build a frequency dictionary from string t.
#  2. Loop through each character in s, decreasing the count in the dictionary.
#  3. Remove characters from the dictionary when their count hits zero.
#  4. At the end, the remaining key in the dictionary is the extra character.

# 📌 Key Logic: Use a hashmap (dictionary) to track frequency and identify the added character efficiently.

# Time Complexity: O(n) – One pass over each string.
# Space Complexity: O(1) – Limited to lowercase letters (max 26 characters).

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)  # length of number list
        prev = nums[0]
        result = []
        for i in range(1, n):
            if (prev == nums[i]):
                nums[i-1] = 2*nums[i-1]
                nums[i] = 0
            prev = nums[i]

        for i in range(n):
            if (nums[i]):
                result.append(nums[i])

        remaining = [0] * (len(nums) - len(result))
        result = result+remaining
        return result


# Problem: [2460. Apply Operations to an Array]
# Highlight: For each i, if nums[i] == nums[i+1], double nums[i], set nums[i+1] = 0. After all operations, move all zeros to the end.

# 💡 My Approach:

# Loop through the array from 0 to n:
#   If adjacent elements are equal, double the first and zero out the second.
# After all operations, create a new list:
#   Add all non-zero values.
# Then, add zeros to the end to maintain array length.

# Key Logic: Perform in-place operations as per the rule, and clean up by filtering non-zeros and padding with zeros at the end.

# ⏱ Time Complexity: O(n) – Two passes through the array.
# 📦 Space Complexity: O(n) – To store the result array

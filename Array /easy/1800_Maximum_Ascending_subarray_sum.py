class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = []
        res = nums[0]
        for i in range(1, len(nums)):
            if (nums[i-1] < nums[i]):
                res += nums[i]
            else:
                result.append(res)
                res = nums[i]
        result.append(res)

        if (len(result) == 0):
            return res

        else:
            return max(result)

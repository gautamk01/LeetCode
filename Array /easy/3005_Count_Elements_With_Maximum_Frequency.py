class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if (dic.get(nums[i])):
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
        valu = list(dic.values())
        maximum = max(valu)
        counter = valu.count(maximum)
        return counter*maximum

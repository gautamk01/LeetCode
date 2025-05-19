class Solution:
    def check(self, nums: List[int]) -> bool:
        demi = nums + nums
        print(demi)
        pointer = 0
        counter = 1
        for i in range(1, len(demi)):
            if (counter == len(nums)):
                return True
            if (demi[i-1] > demi[i]):
                counter = 0
            counter += 1

        return False

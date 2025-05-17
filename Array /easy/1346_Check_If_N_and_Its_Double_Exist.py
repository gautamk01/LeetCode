class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen_number = set()
        count = 0
        for i in arr:
            if ((2*i in seen_number) or (i % 2 == 0 and i/2 in seen_number)):
                return True
            seen_number.add(i)
        return False

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0: -1}#Intialise the hashmap with the 0 and -1 to avoid edge cases
        total = 0
        for i, n in enumerate(nums):
            total+= n
            r = total% k
            if r not in remainder:
                remainder[r] = i
            elif i- remainder[r]> 1:
                return True
        return False
        
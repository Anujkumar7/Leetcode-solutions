class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        maxx = -10**4
        for i in range(0,len(nums)):
            summ += nums[i]
            maxx = max(summ,maxx)
            if summ <0:
                summ = 0
        
        return maxx
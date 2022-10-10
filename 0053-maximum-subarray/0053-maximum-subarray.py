class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        maxx = nums[0]
        for i in range(len(nums)):
            #Step1
            summ += nums[i]
            #Step2
            maxx = max(summ,maxx)
            #Step3
            if summ <0:
                summ = 0
        
        return maxx
    #TC- O(N)
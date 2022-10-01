class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
#         LIS = [1]* len(nums)
        
#         for i in range(len(nums)-1,-1,-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i]< nums[j]:
#                     LIS[i] = max(LIS[i], 1+ LIS[j])
#         return max(LIS)
    
    #DP with Binary solution
        f = []
        for i in range(len(nums)):
        #If the ele in nums is greater than the ele in f
        #append that ele
            if not f or nums[i]> f[-1]:
                f.append(nums[i])
        #If ele is less, then find that particular index of that ele    
            else:
                index = bisect.bisect_left(f, nums[i])
                f[index] = nums[i]
        return len(f)
        
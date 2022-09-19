class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
     # i is for index and a is for values and enumerate is for keeping a counter
        for i, a in enumerate (nums):
            
     # if we found same ele twice, just continue       
            if i> 0 and a== nums[i-1]:
                continue
            
          #Two sum -II algo  
            l, r = i+ 1 , len(nums)- 1
            while l< r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r-=1
                elif threesum < 0:
                    l+=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l< r:
                        l+=1
        return res
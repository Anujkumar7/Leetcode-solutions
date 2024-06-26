class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
  #Optimised solution

        left , right = 0, len(nums)-1
        
        while left <= right:
            mid = (left+ right)//2
            if target== nums[mid]:
                return mid
            
            #Left sorted portion
            if nums[left]<= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left =  mid+1
                else:
                    right =  mid - 1
                    
            #Right sorted portion
            else:
                if target< nums[mid] or target > nums[right] :
                    right = mid - 1
                else:
                    left = mid + 1
                    
        return -1
        
      #Linear traversal algo  TC: O(n)  and SC: 0(1) 
    
            # if target not in nums:
            #     return -1
            # else:
            #     a=nums.index(target)
            #     return a
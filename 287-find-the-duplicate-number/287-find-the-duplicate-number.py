class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast =0, 0
        while True:
            slow =  nums[slow]
            fast = nums[nums[fast]]
            #If both slow and fast meet, means cycle exist so break here 
            if slow== fast:
                break
            
        slow2 = 0
        while True:
            slow= nums[slow]
            slow2 = nums[slow2]
            if slow== slow2:
                return slow
        
        
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i]== nums[i-1]:
        #         return nums[i]
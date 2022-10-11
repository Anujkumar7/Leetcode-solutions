class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        left = sys.maxsize
        mid = sys.maxsize
        for i in range(len(nums)):
            if nums[i]> mid:
                return True
            elif (nums[i]> left and nums[i]< mid):
                mid = nums[i]
            elif (nums[i]< left):
                left = nums[i]
        return False
        
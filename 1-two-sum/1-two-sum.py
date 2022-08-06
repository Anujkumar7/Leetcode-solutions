class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         for i in range(len(nums)):
            left = nums[i+1:]
            for j in range(len(left)):
                if (nums[i] + left[j]) == target:
                    return i, j+i+1
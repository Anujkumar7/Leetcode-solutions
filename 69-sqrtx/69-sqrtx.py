class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 1, x
        
        # Repeat until the pointers low and high meet each other
        
        while low <= high:
            mid = (low + high) // 2             # middle point - pivot
            if mid * mid == x: return mid        # found result
            elif mid * mid < x: low = mid + 1;    # go right side
            else: high = mid - 1                # go left side
        
        return low-1
        
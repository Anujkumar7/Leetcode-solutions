class Solution:
    def maxArea(self, height: List[int]) -> int:
        #BRUTE FORCE
        
#         res = 0
#         for L in range(len(height)):
#             for r in range(L+1, len(height)):
                
#                 #area of a rectangle
#                 area = (r- L) * min(height[L], height[r])
#                 res = max(area, res)
#         return res
    
    #Optimised soln
        res = 0
        l,r = 0, len(height)-1
        while l< r:
            #area of rectangle is height* breadth
            #breadth  = (r-l) and the height is the bottleneck of the both heights meaning min of both heights min(height[l], height[r])
            
            area = (r- l) * min(height[l], height[r])
            res = max(res, area)
            
            if height[l]< height[r]:
                l+=1
            else:
                r-=1
        return res
        
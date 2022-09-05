class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
       #last index nums[1] 
        m, n,last = m-1, n-1, m+n-1 
        
      #Start merging from reverse order  
        while n>=0 and m>=0:
            if nums1[m]> nums2[n]:
                nums1[last] = nums1[m]
                m-=1
            else:
                nums1[last]= nums2[n]
                n-=1
            last-=1
         #For edge case: Fill nums[1] with leftover nums[2] elements 
        if n >-1:
            nums1[0:n+1] = nums2[0:n+1]
                
        
        
        
        
        # j=0
        # for i in range(m,m+n):
        #     nums1[i]=nums2[j]
        #     j+=1
        # nums1.sort()
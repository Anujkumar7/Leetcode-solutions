class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #Iterating from last
        col,row = 0,len(matrix)-1
        
        while row>=0 and col< len(matrix[0]):
            mid = matrix[row][col]
            
#When we know we decreased the search space , now we can apply binary search.
            if mid>target:
                row-=1
                
            elif mid<target:
                col+=1
            else:
                return True
        return False
        
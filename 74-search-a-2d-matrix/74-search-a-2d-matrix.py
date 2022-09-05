class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        
    #BINARY SEARCH:    
    
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1  #low ,end == start end==  start =0, end = [(row*col)-1]== last element of the matrix
        
        while low <= high:
            mid = (low + high) // 2
    
 #For accessing a element in a matrix, we need 2 things row inex and col index
#For row index = index no. / total no. of cols
#For col index = index % total no. of cols
            num = matrix[mid // cols] [mid % cols]
            
            #Implementing Binary search
            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False 
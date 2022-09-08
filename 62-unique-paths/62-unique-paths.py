class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # We initialise from the bottom row
        row = [1]* n
        
        #For iterating in other rows
        for i in range(m - 1):
            
            #Newrow will be above the row
            newRow = [1] * n
            
#for avoiding any edge case we keep a check on our column and we iterate from the right to left
            
            for j in range(n - 2 , -1 , -1):
                newRow[j] = newRow[j+ 1] + row[j] # row[j] is prev row
                #Updating row
            row = newRow
        return row[0]
    
    #TC: 0(n * m)  SC: O(n)                
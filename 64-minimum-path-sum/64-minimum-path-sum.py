class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #Bottom up approach
        
        n = len(grid)
        m = len(grid[0])
        dp = [[0]* m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i ==0 and j==0:
                    dp[i][j] = grid[i][j]
                else:
                    up = grid[i][j]
                    left = grid[i][j]
                    
                    if i> 0: #if i is out of bound
                        up+= dp[i-1][j]
                    else:
                        up+= sys.maxsize
                    
                    if j>0: # if j is out of bound
                        left+= dp[i][j-1]
                    else:
                        left+= sys.maxsize
                        
                        #return the min of up and left
                    dp[i][j] =  min(up, left)
        return dp[n-1][m-1]
                    
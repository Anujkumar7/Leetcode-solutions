class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
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
                    if i> 0:
                        up+= dp[i-1][j]
                    else:
                        up+= sys.maxsize
                    if j>0:
                        left+= dp[i][j-1]
                    else:
                        left+= sys.maxsize
                    dp[i][j] =  min(up, left)
        return dp[n-1][m-1]
                    
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = []
        t = s[::-1]
        
        L= len(s)
        
        #Intialisation
        for _ in range(L+1):
            dp.append([0]*(L+1))
            
        for i in range(1, L+1):
            for j in range(1, L+1):
                if s[i-1]== t[j-1]:
                    dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[L][L]
        
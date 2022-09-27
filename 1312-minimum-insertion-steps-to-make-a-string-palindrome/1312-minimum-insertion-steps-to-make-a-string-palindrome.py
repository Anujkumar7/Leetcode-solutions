class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for i in range(n + 1)]
                
# We are using both for loops with n because we  have given only one string
        for i in range(n):
            for j in range(n):
                if s[i]==s[~j]:
                    dp[i+1][j+1] = 1+ dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j + 1], dp[i + 1][j])
        return n - dp[n][n]
    
# Brief explanation for s[~j].
# ~j = -j - 1
# so while i ranges from 0 to n-1,
# ~i ranges from -1 to -n.
# This is nice because we can now traverse the list backward.
# no need to write for i in range(len(n-1), 0, -1).
        
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        #Bottom up approach
        dp = [[0 for _ in range(target+1)] for _ in range(d)]
        dp[0][0] = 0
        for i in range(1, min(f, target)+1):
            dp[0][i] = 1

        for z in range(1, d):
            for i in range(1, target + 1):
                for x in range(1, f+1):
                    if i - x >= 0:
                        dp[z][i] += dp[z - 1][i - x]

        return dp[-1][-1] % 1000000007

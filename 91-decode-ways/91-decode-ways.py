class Solution:
    def numDecodings(self, s: str) -> int:
        
        #""RECURSION + MEMO"" 
        
        dp = { len(s): 1}
        def dfs(i):
            #Base case
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            res = dfs(i+1)
# If the first digit is 1 then we have limitations for next digits from ("0-9") and if the second digit is 2 then we have limitaions for next digits are ("0-6")

            if (i+1 < len(s) and (s[i] == "1" or
                s[i] == "2" and s[i+1] in "0123456")):
                res += dfs(i+2)
            dp[i] = res
            return res
        
        return dfs(0)
        
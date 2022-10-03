class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev = 0
        ans = 0
        for i in range(1, len(colors)):
            if (colors[i] == colors[prev]):
                if (neededTime[prev]< neededTime[i]):
                    ans+= neededTime[prev]
                    prev = i
                else:
                    ans+= neededTime[i]
            else:
                prev = i
        return ans
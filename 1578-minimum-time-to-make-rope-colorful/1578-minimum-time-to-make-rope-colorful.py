class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev = 0
        ans = 0
        for i in range(1, len(colors)):
            
            # If the prev index character == current character 
            if (colors[i] == colors[prev]):
                
#Then compare the needed time of both if the needed time of prev is less than the current one add that into ans
                if (neededTime[prev]< neededTime[i]):
                    ans+= neededTime[prev]
                    prev = i
#Else update the ans as the current char needed time
                else:
                    ans+= neededTime[i]
#If the prev char != currrent char then update the prev variable with the curr i           
            else:
                prev = i
        return ans
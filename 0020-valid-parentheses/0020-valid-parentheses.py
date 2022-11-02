class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')':'(', '}':'{',']':'['}
        stack = []
        for c in s:
            if c in closeToOpen:
                #stack[-1] means the the last value added to the stack
                if stack and stack[-1]== closeToOpen[c]:
                    stack.pop()
                #If they dont match each other or if the stack is empty
                else:
                    return False
            #If we get an open parenthesis
            else:
                stack.append(c)
        return True if not stack else False
                    
            
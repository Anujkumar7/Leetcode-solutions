class Solution:
    def myPow(self, x: float, n: int) -> float:
        partialans= pow(x,n-1)
        if n ==0:
            return 1
        
        else:
            return x*partialans
            
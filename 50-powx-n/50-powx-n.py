class Solution:
    def myPow(self, x: float, n: int) -> float:
        temp = pow(x,n-1)
        if n==0:
            return 1
        else:
            return x*temp
            
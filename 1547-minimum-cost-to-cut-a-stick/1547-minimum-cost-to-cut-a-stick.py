import sys
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        #Memoiation
        d= {}
        def solve(i,j):
            if (i,j) in d:
                return d[(i,j)]
            ans = sys.maxsize
            cost = j-i
            for cut in cuts:
                if cut<j and cut> i:
                    ans = min(ans , solve(i, cut)+ solve(cut, j)+ cost)
            if ans == sys.maxsize:
                d[(i,j)] =0
            else:
                d[(i,j)] = ans
            return d[(i,j)]
        return solve(0,n)
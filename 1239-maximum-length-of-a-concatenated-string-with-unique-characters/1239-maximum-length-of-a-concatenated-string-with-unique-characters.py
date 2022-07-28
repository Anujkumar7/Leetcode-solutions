class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charset = set()
        
        
#Overlap function is our helper function to finding out that the occurence of char is not more than 1
        def overlap(charset, s):
            # c = Counter(charset)+counter(s)
            # return max(c.values())>1
            prev =set()
            for c in s:
                if c in charset or c in prev:
                    return True
                prev.add(c)
            return False
        
        def backtrack(i):
            if i== len(arr):
                return len(charset)
            
            res=0

#if condition for appending the char and making sure by the overlap function that it doesnot contain nay duplicates

            if not overlap(charset,arr[i]):
                for c in arr[i]:
                    charset.add(c)
                res = backtrack(i+1)
                for c in arr[i]:
                    charset.remove(c)
            return max(res,backtrack(i+1))
        return backtrack(0)
        
        
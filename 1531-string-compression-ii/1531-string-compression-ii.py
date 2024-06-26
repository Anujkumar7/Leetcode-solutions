class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        rle = lambda x: x if x <= 1 else int(log10(x)) + 2 # rle length of a char repeated x times
        @cache 
        
        def fn(i, k, prev, cnt):
            """Return length of rle of s[i:] with k chars to be deleted."""
            if k < 0: return inf 
            if i == len(s): return 0 
            ans = fn(i+1, k-1, prev, cnt) # delete current character 
            if prev == s[i]: 
                ans = min(ans, fn(i+1, k, s[i], cnt+1) + rle(cnt+1) - rle(cnt))
            else: 
                ans = min(ans, fn(i+1, k, s[i], 1) + 1)
            return ans 
        
        return fn(0, k, "", 0)
        
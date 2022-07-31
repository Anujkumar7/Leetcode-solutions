class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPal(l, r):
            return s[l:r] == s[r:l:-1]                      
            
        l, r = 0, len(s) - 1
        skip = 0
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isPal(l, r - 1) or isPal(l + 1, r)
        return True
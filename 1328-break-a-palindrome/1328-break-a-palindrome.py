class Solution:
    def breakPalindrome(self, S: str) -> str:
        for i in range(len(S) // 2):
            if S[i] != 'a':
                return S[:i] + 'a' + S[i + 1:]
        return S[:-1] + 'b' if S[:-1] else ''
        
        # n= len(palindrome)
        # if (n<= 1):
        #     return ""
        # for i in range(n//2):
        #     if (palindrome[i]!= 'a'):
        #         palindrome[i] = 'a'
        #         return palindrome
        # palindrome[n-1] = 'b'
        # return palindrome
                
         
        
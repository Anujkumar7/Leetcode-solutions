class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        
        #Used two pointers l = 0 and with r we are iterating on len(s)
        for r in range(len(s)):
            
        #If duplicate character found in charset we remove the leftmost element   
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res, r- l +1)
        return res
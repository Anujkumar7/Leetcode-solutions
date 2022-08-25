class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s, i = sorted(ransomNote), 0
        for c in sorted(magazine):
            i += i<len(s) and s[i]==c
        return i==len(s)
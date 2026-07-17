class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charsOfS = {}
        charsOfT = {}
        
        for i in range(len(s)):
            charsOfS[s[i]] = 1 + charsOfS.get(s[i], 0)
            charsOfT[t[i]] = 1 + charsOfT.get(t[i], 0)
        
        for letter in charsOfS:
            if charsOfS[letter] != charsOfT.get(letter, 0):
                return False
        return True
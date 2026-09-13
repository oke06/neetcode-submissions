class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        smap, tmap = {}, {}
        for letter in s:
            smap[letter] = smap.get(letter, 0) + 1
        for letter in t:
            tmap[letter] = 1 + tmap.get(letter, 0)
        
        for letter in smap:
            if smap[letter] != tmap.get(letter, 0):
                return False
        return True
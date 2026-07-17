class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        dict_t, dict_s = {}, {}
        for i in range(len(s)):
            dict_t[t[i]] = 1 + dict_t.get(t[i], 0)
            dict_s[s[i]] = 1 + dict_s.get(s[i], 0)
        
        for letter in dict_t:
            if dict_t[letter] != dict_s.get(letter, -1):
                return False
        return True
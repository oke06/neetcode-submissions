class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = []
        list_t = []
        for letter in s:
            list_s.append(letter)
        list_s.sort()
        for letter in t:
            list_t.append(letter)
        list_t.sort()
        if list_t == list_s:
            return True
        return False
        
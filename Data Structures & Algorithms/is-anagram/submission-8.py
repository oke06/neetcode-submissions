class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCount, tCount = {},{}

        for letter in s:
            sCount[letter] = sCount.get(letter, 0) + 1
        for letter in t:
            tCount[letter] = tCount.get(letter, 0) + 1
        for letter in sCount:
            if sCount[letter] != tCount.get(letter, 0):
                return False
        return True
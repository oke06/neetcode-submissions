class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)
        s1_count = [0] * 26 
        for c in s1:
            s1_count[ord(c) - ord('a')] += 1
        
        while r <= len(s2):
            window = s2[l:r]
            window_count = [0] * 26
            for c in window:
                window_count[ord(c) - ord('a')] += 1
            if all(window_count[i] == s1_count[i] for i in range(26)):
                return True
            else:
                l += 1
                r += 1
        return False 


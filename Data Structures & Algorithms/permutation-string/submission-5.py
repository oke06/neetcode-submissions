class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l, r = 0, len(s1)
        s1_count = {}
        window_count = {}
        
        for i in range(len(s1)):
            s1_count[s1[i]] = 1 + s1_count.get(s1[i], 0)
            window_count[s2[i]] = 1 + window_count.get(s2[i], 0)

        if s1_count == window_count:
            return True

        for j in range(len(s1), len(s2)):
            window_count[s2[j - len(s1)]] -= 1
            if window_count[s2[j - len(s1)]] == 0:
                del window_count[s2[j - len(s1)]]
            window_count[s2[j]] = 1 + window_count.get(s2[j], 0)
            if window_count == s1_count:
                return True

        return False
        


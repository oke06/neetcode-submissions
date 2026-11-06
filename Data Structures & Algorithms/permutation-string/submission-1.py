class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = "".join(sorted(s1))
        l, r = 0, len(s1)
        while r < len(s2) + 1:
            window = s2[l:r]
            sorted_window = "".join(sorted(window))
            if sorted_window == sorted_s1:
                return True
            l += 1
            r += 1

        return False
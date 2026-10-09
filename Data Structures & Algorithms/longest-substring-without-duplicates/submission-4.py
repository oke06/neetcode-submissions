class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        res = 0
        while l < len(s):
            if r < len(s) and s[r] not in s[l:r]:
                res = max(res, len(s[l:r]))
                r += 1
            else:
                l += 1
        return 0 if len(s) == 0 else res + 1
        
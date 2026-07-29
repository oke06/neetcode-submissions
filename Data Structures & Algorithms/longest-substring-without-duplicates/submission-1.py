class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        if len(s) <= 1:
            return len(s)
        res = 1
        while r < len(s):
            if s[r] in s[l:r]:
                l += 1
                r = l + 1
                continue  
            res = max(res, len(s[l:r+1]))
            r += 1
        return res
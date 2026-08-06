class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        res = 0

        while l < r:
            if lmax < rmax:
                res += (lmax - height[l + 1]) if lmax - height[l+1] >= 0 else 0
                l += 1
                lmax = max(height[l], lmax)   
            else:
                r -= 1
                rmax = max(height[r], rmax)
                res += rmax - height[r]

        return res
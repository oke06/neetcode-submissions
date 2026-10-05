class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[l] < nums[r]:
                return nums[l]
            
            if nums[mid] >= nums[l]:
                l += 1
            else:
                r -= 1
        return nums[mid]
        
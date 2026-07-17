class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        digits = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in digits:
                return [digits[diff], i]
            digits[num] = i
        return
            
        
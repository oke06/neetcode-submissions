class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        passed = {}
        for i, num in enumerate(nums):
            if target - num in passed:
                return [passed[target - num], i]
            else:
                passed[num] = i
        

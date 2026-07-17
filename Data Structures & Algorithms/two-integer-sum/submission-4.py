class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counted = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in counted:
                return [counted[diff], i]
            else:
                counted[v] = i
        return []
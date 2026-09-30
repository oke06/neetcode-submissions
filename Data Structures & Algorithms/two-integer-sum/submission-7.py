class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        appeared = {} 
        for i, n in enumerate(nums):
            diff = target - n
            if diff in appeared:
                return [appeared[diff], i]
            appeared[n] = i
        return False
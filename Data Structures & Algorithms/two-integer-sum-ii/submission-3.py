class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indexes = {}
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in indexes:
                return [indexes[diff] + 1, i + 1]
            indexes[n] = i
        return []
        
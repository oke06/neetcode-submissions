class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked = set()
        for num in nums:
            if num not in checked:
                checked.add(num)
            else:
                return True
        return False
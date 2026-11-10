class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        repeats = set()
        for n in nums:
            if n in repeats:
                return n
            repeats.add(n)

        
        
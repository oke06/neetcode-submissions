class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = [1]
        if len(nums) == 0:
            return 0
        for num in nums:
            count = 1
            cur = num
            flag = True
            while flag:
                cur += 1 
                if cur in nums:
                    count += 1
                else:
                    flag = False
            longest.append(count)
        return max(longest)
            
             

        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            leftprod = 1
            rightprod = 1
            j = 0
            k = len(nums) - 1  
            while j != i:
                leftprod *= nums[j]
                j += 1
            while k != i:
                rightprod *= nums[k]
                k -= 1
            output.append(leftprod * rightprod)
        return output
        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        index = -1
        while l<= r:
            mid = (l + r) // 2
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                index = mid
                break
        
        if index == -1:
            return False
        
        left, right = 0, len(matrix[index]) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[index][mid]:
                left = mid + 1
            elif target < matrix[index][mid]:
                right = mid - 1
            else:
                return True
        return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                break
        
        left, right = 0, len(matrix[mid]) - 1
        while left <= right:
            m = (left + right) // 2
            if matrix[mid][m] < target:
                left = m + 1
            elif matrix[mid][m] > target:
                right = m - 1
            else:
                return True
        return False
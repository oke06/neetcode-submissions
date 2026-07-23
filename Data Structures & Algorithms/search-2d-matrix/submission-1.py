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

        if l > r:
            return False
        i = (l+r)//2
        newl, newr = 0, len(matrix[i])
        while newl <= newr:
            mid = (newl + newr) // 2
            if target > matrix[i][mid]:
                newl = mid + 1
            elif target < matrix[i][mid]:
                newr = mid - 1
            else:
                return True
        return False
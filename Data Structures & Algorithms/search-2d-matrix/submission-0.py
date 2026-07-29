class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        cells = rows * cols

        low = 0
        high = cells - 1

        while low <= high:
            mid = low + ((high - low) // 2)
            midRow = mid // cols
            midCol = mid % cols
            val = matrix[midRow][midCol]
            if val < target:
                low = mid + 1
            elif val > target:
                high = mid - 1
            else:
                return True
        return False
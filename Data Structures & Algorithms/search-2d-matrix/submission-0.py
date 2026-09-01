class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS = len(matrix), len(matrix[0])
        lo, hi = 0, ROWS*COLS - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid // COLS][mid % COLS] < target:
                lo = mid + 1
            elif matrix[mid // COLS][mid % COLS] > target:
                hi = mid - 1
            else:
                return True

        return False
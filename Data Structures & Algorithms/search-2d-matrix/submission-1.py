class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        row = -1

    # First binary search: find the correct row
        while low <= high:
            mid = (low + high) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif target > matrix[mid][-1]:
                low = mid + 1
            else:  # target < matrix[mid][0]
                high = mid - 1

        if row == -1:
            return False

    # Second binary search: search inside that row
        low = 0
        high = len(matrix[row]) - 1

        while low <= high:
            mid = (low + high) // 2

            if matrix[row][mid] == target:
                return True
            elif target > matrix[row][mid]:
                low = mid + 1
            else:
                high = mid - 1

        return False
                
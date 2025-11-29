class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            index = bisect_left(matrix[i], target)
       
            if index < len(matrix[i]) and matrix[i][index] == target:
                return True
        return False
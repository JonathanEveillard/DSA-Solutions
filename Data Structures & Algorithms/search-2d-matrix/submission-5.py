class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while i < len(matrix):
            low = 0
            high = len(matrix[i]) - 1

            j = 0
            while j < len(matrix):
                while low <= high:
                    mid = (high + low) // 2
                    guess = matrix[i][mid]
                    
                    if guess == target:
                        return True
                    if guess < target:
                        low = mid + 1
                    else:
                        high = mid - 1
                j += 1
            i += 1
        return False
            
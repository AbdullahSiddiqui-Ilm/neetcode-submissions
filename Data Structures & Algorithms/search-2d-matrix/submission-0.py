class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (r + l) // 2
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                l, r = 0, len(matrix[m]) - 1
                while l <= r:
                    m2 = (r + l) // 2
                    if matrix[m][m2] > target:
                        r = m2 - 1
                    elif matrix[m][m2] < target:
                        l = m2 + 1
                    else:
                        return True
        return False

                



            

        
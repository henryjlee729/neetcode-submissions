class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowsToZero = set()
        colsToZero = set()
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):
                if matrix[row][col] == 0:
                    rowsToZero.add(row)
                    colsToZero.add(col)

        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):
                if row in rowsToZero or col in colsToZero:
                    matrix[row][col] = 0
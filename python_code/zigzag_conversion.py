class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows == len(s):
            return s
        matrix = [''] * numRows
        row = step = 0
        for i in s:
            matrix[row] += i
            if row == 0:
                step = 1
            if row == numRows - 1:
                step = -1
            row += step
        return ''.join(matrix)

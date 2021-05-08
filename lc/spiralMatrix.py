# https://leetcode.com/problems/spiral-matrix/submissions/

def spiralOrder(self, matrix):
    row_start, col_start, row_end, col_end = 0,0, len(matrix), len(matrix[0])
    output = []
    while row_start < row_end and col_start < col_end:
        for i in range(col_start, col_end):
            output.append(matrix[row_start][i])
        row_start +=1
        for i in range(row_start, row_end):
            output.append(matrix[i][col_end -1])
        col_end -=1
        if row_start < row_end:
            for i in range(col_end -1, col_start -1, -1):
                output.append(matrix[row_end -1][i])
            row_end -=1
        if col_start < col_end:
            for i in range(row_end -1, row_start -1, -1):
                output.append(matrix[i][col_start])
            col_start +=1
    return output

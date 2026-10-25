# https://leetcode.com/problems/set-matrix-zeroes/

# class Solution:
#     def setZeroes(self, matrix: list[list[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
        
#         rows = len(matrix)
#         cols = len(matrix[0])

#         list_index = []
#         for i in range(rows):
#             for j in range(cols):
#                 if matrix[i][j] == 0:
#                     list_index.append((i,j))        
        
#         for index in list_index:
#             x,y = index[0], index[1]

#             for col in range(cols):
#                 matrix[x][col] = 0
#             for row in range(rows):
#                 matrix[row][y] = 0


"""
m = number of rows, and 
n = number of columns in the matrix.

T.C.: O(mn(m+n))
S.C.: O(mn)

Approach:
1. Traverse the matrix and store the coordinates of all zero elements.
2. For each stored coordinate, set its entire row and column to zero.

"""



# class Solution:
#     def setZeroes(self, matrix: list[list[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
        
#         rows = len(matrix)
#         cols = len(matrix[0])

#         row_val = [False] * rows
#         col_val = [False] * cols
#         for i in range(rows):
#             for j in range(cols):
#                 if matrix[i][j] == 0:
#                     row_val[i] = True
#                     col_val[j] = True        
        
#         for i in range(rows):
#             if row_val[i]:
#                 for index in range(cols):
#                     matrix[i][index] = 0
                
#         for j in range(cols):
#             if col_val[j]:
#                 for index in range(rows):
#                     matrix[index][j] = 0

"""

T.C -> O(mn)
S.C -> O(m+n)
Approach: Two-Pass Matrix Traversal + Row/Column Marker Arrays


"""


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))


        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0


        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
    
"""
T.C -> O(mn)
S.C -> O(1)

Approach: 

1. Save the original first-row and first-column states.
2. Mark rows and columns using the first row and column.
3. Zero out the interior cells.
4. Zero out the first row if first_row_zero is True.
5. Zero out the first column if first_col_zero is True.


"""
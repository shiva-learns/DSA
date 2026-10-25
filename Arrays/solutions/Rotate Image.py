# https://leetcode.com/problems/rotate-image/

# class Solution:
#     def rotate(self, matrix: list[list[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix)
        
#         # temp = [[0]*n] * n
#         temp = [[0] * n for _ in range(n)]
        
#         for i in range(n):
#             for j in range(n):
#                 temp[j][n-1-i] = matrix[i][j]
        
        
#         for i in range(n):
#             for j in range(n):
#                 matrix[i][j] = temp[i][j]

"""
# Approach: Using an Extra Matrix
# T.C: O(n²)
# S.C: O(n²) Auxiliary Space

"""




class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            #     print([(i,j),(j,i)])
            # print()



        for i in range(n):
            matrix[i].reverse()

"""
Approach: Matrix Transposition + Row Reversal
T.C: O(n^2)
S.C: O(1) Auxiliary Space
"""
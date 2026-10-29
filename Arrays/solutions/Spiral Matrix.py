# https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []


        m = len(matrix)
        n = len(matrix[0])

        top,bottom,left,right = 0,m-1,0,n-1
        element_list = []

        while top<=bottom and left<=right:

            for i in range(left,right+1):
                element_list.append(matrix[top][i])
            top += 1
            
            for j in range(top,bottom+1):
                element_list.append(matrix[j][right])
            right -= 1
            
            if top<=bottom:
                for k in range(right,left-1,-1):
                    element_list.append(matrix[bottom][k])
                bottom -= 1

            if left <= right:
                for l in range(bottom,top-1,-1):
                    element_list.append(matrix[l][left])
                left += 1
            
            print(top,bottom)
            

        return element_list

"""        
T.C -> O(n*m)
S.C -> O(n*m)
Boundary Traversal (Simulation) — Spiral Matrix

"""
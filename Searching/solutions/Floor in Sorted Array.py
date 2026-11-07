# https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1

# class Solution:
#     def findFloor(self, arr, x):
#         # code here
        
#         n = len(arr)
#         if n == 0:
#             return -1
        
#         temp1 = -1
        
#         for i in range(n):
#             if arr[i] <= x:
#                 temp1 = i
            
#         return temp1

"""
T.C -> O(n)
S.C -> O(1)
Approach: Using Linear Search

"""
            
    

class Solution:
    def findFloor(self, arr, x):
        # code here
        
        n = len(arr)
        low = 0
        high = n - 1
        
        fl = -1
        
        while (low <= high):
            mid = (low+high)//2

            if (arr[mid]<=x):
                fl = mid
                low = mid + 1
            
            else:
                high = mid - 1
        
        return fl
        
"""
T.C -> O(logn)
S.C -> O(1)
Approach: Binary Search

"""
            
            
            
            
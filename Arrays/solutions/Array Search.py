# https://www.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1


class Solution:
    def search(self, arr, x):
        # code here
        
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1
        

"""

T.C -> O(n)
S.C -> O(1)

Approach: Iterate through Loop

"""
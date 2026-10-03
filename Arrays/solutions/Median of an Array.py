# https://www.geeksforgeeks.org/problems/find-the-median0527/1?utm=codolio
class Solution:
    def findMedian(self, arr):
        #code here.
        n = len(arr)
        arr.sort()
        
        if n % 2 != 0:
            val = arr[n//2]
        else:
            val =  (arr[n//2-1]+arr[n//2])/2
        return val
        
"""
T.C -> O(nlogn) 
S.C -> O(1)

Approach:  First sort then, find the median


"""
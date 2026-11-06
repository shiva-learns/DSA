# https://www.geeksforgeeks.org/problems/implement-lower-bound/1

class Solution:
    def lowerBound(self, arr, target):
        # code here
        n = len(arr)
        lb = n
        
        low, high = 0, n-1
        
        while (low<=high):
            mid = (low+high)//2
            
            if (arr[mid]>=target):
                lb = mid
                high = mid - 1
            
            else:
                low = mid + 1
        
        return lb

"""
T.C -> O(logn)
S.C -> O(1)
Approach: Binary Search


"""
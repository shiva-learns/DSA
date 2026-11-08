# https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1
class Solution:
    def countFreq(self, arr, target):
        # code here
        
        n = len(arr)
        
        def upperbound():
            low = 0
            high = n - 1
            
            ub = -1
            while (low<=high):
                mid = (low+high)//2
                
                if (arr[mid]>=target):
                    ub = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ub
        
        def floor():
            low = 0
            high = n-1
            
            fl = -1
            while (low <= high):
                mid = (low + high)//2
                
                if (arr[mid]<=target):
                    fl = mid
                    low = mid + 1
                    
                else:
                    high = mid - 1
                
            return fl
        
        ub, fl = upperbound(),floor()
        
        if ub == -1 or arr[ub] != target:
            return 0
        
        return (fl-ub)+1
                
                
                
"""
T.C -> O(logn)
S.C -> O(1)
Approach: Two Binary Search

"""
                
                
                
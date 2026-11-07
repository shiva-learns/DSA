# https://www.naukri.com/code360/problems/ceiling-in-a-sorted-array_1825401?leftPanelTabValue=SUBMISSION
def getFloorAndCeil(a, n, x):
    # Write your code here.

    def ceiling():
        low = 0
        high = n-1

        ub = -1
        while(low<=high):
            mid = (low+high)//2
            
            if a[mid] >= x:
                ub = a[mid]
                high = mid - 1
            else:
                low = mid + 1
        return ub
    
    def floor():
        low = 0
        high = n-1

        fl = -1
        while(low<=high):
            mid = (low+high)//2
            
            if a[mid] <= x:
                fl = a[mid]
                low = mid + 1
            else:
                high = mid - 1
        return fl
    
    return floor(),ceiling()

"""
T.C -> O(logn)
S.C -> O(1)
Approach: Binary Search (Upper bound and Floor)

"""
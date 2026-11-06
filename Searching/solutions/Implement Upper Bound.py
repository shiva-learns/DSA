# https://www.naukri.com/code360/problems/implement-upper-bound_8165383?leftPanelTabValue=SUBMISSION

def upperBound(arr: [int], x: int, n: int) -> int: #type: ignore
    # Write your code here.
    n = len(arr)
    ub = n
    low, high = 0, n-1

    while(low<=high):
        mid = (low+high)//2
        
        if (arr[mid]>x):
            ub = mid
            high = mid-1
        
        else:
            low = mid+1
        
    return ub

"""
T.C -> O(logn)
S.C -> O(1)
Approach : Binary Search

"""
"""
Solved Two methods : Iterative Process + Recursion

For Iterative
T.C -> O(logn with base 2)
S.C -> O(1)

For Recursion
T.C -> O(logn with base 2)
S.C -> O(logn) [Recursion calls consume stack space]

"""


def binarySearch(arr,target):
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

arr = [2,4,6,7,9,11,18,19]
target = 7
print(binarySearch(arr,target))






# def binarySearch(arr,target,low,high):
#     if low > high:
#         return -1
#     mid = (low + high)//2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] < target:
#         return binarySearch(arr,target,mid+1,high)
#     else:
#         return binarySearch(arr,target,low,mid-1)
    

# arr = [2,4,6,7,9,11,18,19]
# target = 20
# print(binarySearch(arr,target,0,len(arr)-1))
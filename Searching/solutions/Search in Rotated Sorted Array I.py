# https://leetcode.com/problems/search-in-rotated-sorted-array/
# class Solution:
#     def search(self, nums: list[int], target: int) -> int:
#         n = len(nums)
        
#         def pivot(nums,low,high):

#             while (low<=high):
#                 mid = (low+high)//2

#                 if nums[low]<=nums[high]:
#                     return low                

#                 elif (nums[mid] > nums[high]):
#                     low = mid + 1
#                 else:
#                     high = mid
        
#         def binarySearch(nums,low,high,target):
#             while (low <= high):
#                 mid = (low + high)//2

#                 if nums[mid] == target:
#                     return mid
                
#                 elif nums[mid] > target:
#                     high = mid - 1                 
                
#                 else:
#                     low = mid + 1
                
#             return -1
        

#         pindex = pivot(nums,0,n-1)

#         if pindex == 0:
#             return binarySearch(nums,0,n-1,target)

#         elif nums[pindex] == target:
#             return pindex
        
#         elif nums[0] <= target <= nums[pindex-1]:
#             return binarySearch(nums,0,pindex-1,target)
#         return binarySearch(nums,pindex+1,n-1,target)      

"""
T.C -> O(logn)
S.C -> O(1)
Approach: Using Binary Search

"""



def binarySearch(nums,low,high,target):
    while (low <= high):
        mid = (low + high)//2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] > target:
            high = mid - 1                 
        
        else:
            low = mid + 1
        
    return -1

"""
1. Identify the sorted part
2. Checking if that element present in sorted part
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)

        low,high = 0,n-1

        while (low<=high):
            mid = (low+high)//2

            if nums[mid]==target:
                return mid

            elif nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                
                else:
                    high = mid - 1
            
            else:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1


"""
T.C -> O(logn)
S.C -> O(1)

Appraoch: Modified Binary Search – Identify the Sorted Half.
"""
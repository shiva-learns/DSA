# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# class Solution:
#     def search(self, nums: list[int], target: int) -> bool:
#         n = len(nums)
        
#         def pivot(nums,low,high):

#             while (low<=high):
#                 mid = (low+high)//2               

#                 if (nums[mid] > nums[high]):
#                     low = mid + 1
#                 elif nums[mid] < nums[high]:
#                     high = mid
#                 else:
#                     high -= 1
#             return low
        
#         def binarySearch(nums,low,high,target):
#             while (low<=high):

#                 mid = (low+high)//2

#                 if nums[mid] == target:
#                     return mid
                
#                 elif nums[mid] > target:
#                     high = mid - 1
#                 else:
#                     low = mid + 1
            
#             return -1
        
#         pindex = pivot(nums,0,n-1)
#         print(pindex)
        
#         if pindex == 0:
#             val = binarySearch(nums,0,n-1,target)
        
#         elif nums[pindex] == target:
#             val = pindex
        
#         elif nums[0] <= target <= nums[pindex-1]:
#             val = binarySearch(nums,0,pindex-1,target)
#         else:
#             val = binarySearch(nums,pindex+1,n-1,target)        

#         return False if val == -1 else True


class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        n = len(nums)

        low,high = 0,n-1

        while (low<=high):
            mid = (low+high)//2

            if nums[mid]==target:
                return True
            
            elif nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

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
        return False

"""
T.C -> 
Avg: O(logn)
Worst Case: O(n/2)

S.C -> O(1)

Approach: 
Modified Binary Search – Identify the Sorted Half 
with Duplicate Handling (Ambiguous Case Reduction).


"""
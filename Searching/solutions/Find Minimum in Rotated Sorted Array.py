# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        def pivot(nums):
            low = 0
            high = len(nums)-1

            while (low<=high):
                mid = (low+high)//2

                if nums[low] <= nums[high]:
                    return nums[low]

                elif nums[mid] > nums[high]:
                    low = mid + 1
                
                else:
                    high = mid
            
        return pivot(nums) #type: ignore
    
"""
T.C -> O(logn)
S.C -> O(1)
Approach: Finding pivot element using Binary Search


"""
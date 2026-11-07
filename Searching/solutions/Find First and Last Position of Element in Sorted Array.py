# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        if n == 0:
            return [-1,-1]
        
        def lowerBound():
            low = 0
            high = n-1

            lb = -1
            while (low<=high):
                mid = (low+high)//2

                if (nums[mid]>=target):
                    lb = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return lb
        
        def floor():
            low = 0
            high = n-1 

            fl = -1

            while (low<=high):
                mid = (low+high)//2

                if (nums[mid]<=target):
                    fl = mid
                    low = mid+1
                else:
                    high = mid - 1
            return fl
        
        lb, fl = lowerBound(),floor()


        if lb == -1 or nums[lb] != target:
            return [-1, -1]
        
        return [lb,fl]


"""
T.C -> O(logn)
S.C -> O(1)
Approach: Two binary search (Lower + Upper)
"""
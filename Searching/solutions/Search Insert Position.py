# https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)

        low = 0
        high = n-1

        lb = n
        while (low<=high):
            mid = (low+high)//2

            if nums[mid] >= target:
                high = mid - 1
                lb = mid
            
            else:
                low = mid+1
        
        return lb
"""
T.C -> O(logn)
S.C -> O(1)
Approach: Lower Bound

"""
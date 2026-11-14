# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution:
    def check(self, nums: List[int]) -> bool: #type: ignore
        count = 0
        n = len(nums)
        
        for i in range(n):

            if nums[i] > nums[(i+1)%n]:
                count += 1
        
        return True if count <= 1 else False

"""
T.C -> O(n)
S.C -> O(1)

Traverse from the first element to the last element and,
if the next element is smaller than the current element, 
increment count of adjacent inversions by 1.

For the last element, if it is greater than the first element, 
increment count of adjacent inversions by 1.

"""
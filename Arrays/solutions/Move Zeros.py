# https://leetcode.com/problems/move-zeroes/

# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         temp = []

#         for x in nums:
#             if x!=0:
#                 temp.append(x)
        
#         n = len(nums)
#         while (len(temp)!=n):
#             temp.append(0)

#         nums[:]  = temp[:]

"""
Solved using NAIVE APPROACH: 
T.C -> O(n)
S.C -> O(n)

"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return
        
        i = 0
        while i<len(nums):
            if nums[i]==0:
                break
            i += 1
        
        if i == len(nums):
            return # means, no zero exist
        
        j = i+1 # finding non-zero element

        while (j<len(nums)):
            if nums[j]!=0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
            j += 1

"""
T.C -> O(n)
S.C -> O(1)

Approach : 
Two Pointers + In-place Swapping

i - points to the position where the next non-zero element should go.
j - scans ahead to find the next non-zero element.

"""
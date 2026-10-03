# https://leetcode.com/problems/find-the-duplicate-number/?utm=codolio

# class Solution:
#     def findDuplicate(self, nums: list[int]) -> int:

#         count = {}
#         val = n 
#         for x in nums:
#             if x not in count:
#                 count[x] = 1
#             else:
#                 count[x] += 1
#                 val = x
#                 break
        
#         return val

"""

T.C -> O(n)
S.C -> O(n)
Approach -> Used extra space of O(n), and make dictionary

"""

# class Solution:
#     def findDuplicate(self, nums: list[int]) -> int:
#         n = len(nums)
#         for i in range(n):
#             for j in range(i+1,n):
#                 if nums[i] == nums[j]:
#                     return nums[i]
        
        
"""

T.C -> O(n^2)
S.C -> O(1)
Approach -> Using nested LOOP

"""


class Solution:
    def findDuplicate(self, nums):
        slow, fast = nums[0], nums[0]

        # Finds a meeting point inside the cycle.
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast: break

        # Finds the entrance of the cycle, which gives us the duplicate.
        slow = nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow


"""
T.C -> O(n)
S.C -> O(1)

Approach -> Floyd’s Cycle Detection (Tortoise and Hare)


"""
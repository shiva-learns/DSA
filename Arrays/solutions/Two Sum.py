# https://leetcode.com/problems/two-sum/

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
        

#         for i in range(len(nums)):
#             val = target - nums[i]
#             for j in range(i+1,len(nums)):
#                 if nums[j] == val:
#                     return [i,j]

"""
T.C -> O(n^2)
S.C -> O(1)
Approach: Traversing the list Twice

"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i

        for i in range(len(nums)):
            val = (target-nums[i])

            if val in map and map[val]!=i:
                return [i,map[val]]

"""

T.C -> O(n)
S.C -> O(n)

Approach: Using Hash Table

"""
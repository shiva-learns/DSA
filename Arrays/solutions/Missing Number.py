# https://leetcode.com/problems/missing-number/description/

# class Solution:
#     def missingNumber(self, nums: list[int]) -> int:
#         n = len(nums)
        
#         n_list = [x for x in range(n+1)] # T.C -> O(n)
#         val = set(n_list).difference(set(nums))
#         return list(val)[0]


"""

T.C -> O(n)
[for loop O(n) + set(n_list) O(n) + set(nums) O(n) + .difference O(n)]

S.C -> O(n)

"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        
        nth_sum = n*(n+1)//2

        total = 0
        for x in nums:
            total += x
        

        
        return nth_sum - total

"""

T.C -> O(n)
S.C -> O(1)
Approach: Using Sum formula

"""
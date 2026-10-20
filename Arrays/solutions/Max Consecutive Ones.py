# https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_ones = 0
        count = 0

        for x in nums:
            if x == 1:
               count += 1
            else:
                if count > max_ones:
                    max_ones = count
                count = 0 
        if count > max_ones:
            max_ones = count

        return max_ones

"""
T.C -> O(n)
S.C -> O(1)
Approach: Traversing the list and store count

"""
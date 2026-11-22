# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxi = 0

        for x in s:
            if x == "(":
                count += 1
            elif x == ")":
                count -= 1
            maxi = max(count,maxi)
        return maxi
            
            
"""

T.C -> O(n)
S.C -> O(1)
Approach: Counting parentheses

"""
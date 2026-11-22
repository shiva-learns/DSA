# https://leetcode.com/problems/remove-outermost-parentheses/
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        result = ""

        for x in s:
            if x == "(":
                count += 1
                if count != 1:
                    result += x
            elif x == ")":
                count -= 1
                if count != 0:
                    result += x
        return result

"""
T.C -> O(n)
S.C -> O(n)
Approach: Depth Tracking / Counter (Linear Traversal)

"""
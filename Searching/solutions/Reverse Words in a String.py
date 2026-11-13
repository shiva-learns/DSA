# https://leetcode.com/problems/reverse-words-in-a-string/
class Solution:
    def reverseWords(self, s: str) -> str:
        new = s.split() 
        return " ".join(new[::-1])

"""
n -> n is the length of the input string.

T.C -> O(n)
S.C -> O(n)
Approach: Using Built-in String Methods

"""
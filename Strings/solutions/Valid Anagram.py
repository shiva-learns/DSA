# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
"""
T.C -> O(nlogn)
S.C -> O(n)
Approach:
    Sorting
"""
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I':1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        total = 0
        prev = 0
        for x in s:
            if prev < roman[x]:
                total += (roman[x]-2*prev)
            else:
                total += roman[x]
            prev = roman[x]
        
        return total

"""
T.C -> O(n)
S.C -> O(1)
Approach: Greedy / Previous value comparison
"""
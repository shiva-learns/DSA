# https://leetcode.com/problems/largest-odd-number-in-string/description/

# class Solution:
#     def largestOddNumber(self, num: str) -> str:
#         max_odd = 0
#         n = len(num)
#         for i in range(n):
#             for j in range(i+1,n+1):
#                 if int(num[i:j])%2 != 0:
#                     print(num[i:j])
#                     max_odd = max(max_odd,int(num[i:j]))
        
#         return str(max_odd) if max_odd != 0 else ""

# class Solution:
#     def largestOddNumber(self, num: str) -> str:
#         max_odd = 0
#         n = len(num)
        
#         for i in range(n):
#             j = i+1
#             while (j <= n):
#                 # print(j,num[j],num[i:j])
#                 if int(num[i:j])%2 != 0:
#                     max_odd = max(max_odd,int(num[i:j]))
#                     print(num[i:j])
#                     j += 1
#                 else:
#                     break
        
#         return str(max_odd) if max_odd != 0 else ""


class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        
        for i in range(n-1,-1,-1):
            if int(num[i])%2 != 0:
                return num[:i+1]
        return ""

"""
T.C -> O(n)
S.C -> O(1)
Approach: Reverse iteration and slicing

"""
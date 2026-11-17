# https://leetcode.com/problems/longest-common-prefix/

# class Solution:
#     def longestCommonPrefix(self, strs: list[str]) -> str:
#         common = strs[0]
#         m = len(common)
#         n = len(strs)


#         for i in range(1,n):
#             mini_index = min(len(strs[i])-1,len(common)-1)
#             print(mini_index)
#             for j in range(mini_index):
#                 # print(common[j],strs[i][j])
#                 if common[:j+1] == strs[i][:j+1]:
#                     print(common[:j+1])
#                 # print(common[:j+1],strs[i][:j+1])

        
#         # for j in range(len(common)):
#         #     print(j,common[:j+1])


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs)==0:
            return ""
        result = ""
        base = strs[0]

        for i in range(0,len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return result
            result += base[i]
        
        return result

"""
- n = Number of strings.
- m = Length of the first string (base).

T.C -> O(n*m)
S.C -> O(m)

Approach: 
Compare each character of the first string with the corresponding character of all other strings. If a mismatch occurs or a string ends, return the prefix found so far. Otherwise, keep appending matching characters to the result.

"""
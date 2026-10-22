# https://leetcode.com/problems/rearrange-array-elements-by-sign/

# class Solution:
#     def rearrangeArray(self, nums: list[int]) -> list[int]:

#         pos_list, neg_list = [],[]
#         for x in nums:
#             if x >= 0:
#                 pos_list.append(x)
#             else:
#                 neg_list.append(x)       

#         for i in range(len(pos_list)):
#             nums[i*2] = pos_list[i]
#             nums[i*2+1] = neg_list[i]
        
#         return nums

"""
T.C -> O(n)
s.C -> O(n)

Approach : Two-Pass Separation and Alternating Placement

Runtime: 64ms | Beats 25.87 %
Memory : 43mb | Beats 43.02 %

Inplace Modification

"""

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:

        pos_list, neg_list = [],[]
        for x in nums:
            if x >= 0:
                pos_list.append(x)
            else:
                neg_list.append(x)       

        new_list = []
        for i in range(len(pos_list)):
            new_list.append(pos_list[i])
            new_list.append(neg_list[i])
        
        return new_list

"""

T.C -> O(n)
s.C -> O(n)

Approach : Two-Pass Separation and Alternating Placement

Runtime: 47ms | Beats 64.62 %
Memory : 43mb | Beats 25.94 %

No-Inplace Modification

"""
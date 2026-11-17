# https://leetcode.com/problems/isomorphic-strings/

# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         # s_dict = {key:value for key,value in zip(s,t)}
#         # print(s_dict)

#         temp_dict = {}
#         for key,value in zip(s,t):
#             if key in temp_dict.keys():
#                 if temp_dict[key] != value:
#                     return False
#             else:
#                 temp_dict[key] = value
        
#         values = list(temp_dict.values())

#         val_rep = {}
#         for x in values:
#             if x not in val_rep:
#                 val_rep[x] = 1
#             else:
#                 return False
        

#         return True


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # s_dict = {key:value for key,value in zip(s,t)}
        # print(s_dict)

        s_t_dict = {}
        t_s_dict = {}
        for char_s,char_t in zip(s,t):
            if char_s in s_t_dict:
                if s_t_dict[char_s] != char_t:
                    return False
            else:
                s_t_dict[char_s] = char_t

            if char_t in t_s_dict:
                if t_s_dict[char_t] != char_s:
                    return False
            else:
                t_s_dict[char_t] = char_s
        

        return True

"""
T.C -> O(n)
S.C -> O(2n) ~ O(n)

Approach: Using hashmap checking one to one condition


"""
# https://leetcode.com/problems/rotate-string/

# def rotate(string,k):
#         str_list = [x for x in string]

#         def reverse(start,end):
#             while (start<end):
#                 str_list[start],str_list[end] = str_list[end],str_list[start]
#                 start += 1
#                 end -= 1
#         n = len(str_list)
#         k = k%n
        
#         reverse(0, n - 1)    
#         reverse(0, k - 1)
#         reverse(k,n-1)

#         return "".join(str_list)



# class Solution:       

#     def rotateString(self, s: str, goal: str) -> bool:

#         for i in range(len(s)):
#             val = rotate(s,i)
#             if val == goal:
#                 return True
#         return False

"""
T.C -> O(n^2)
S.C -> O(n)
Approach: 
Brute Force – Reversal Algorithm (Repeated String Rotation)

"""


class Solution:       

    def rotateString(self, s: str, goal: str) -> bool:

        return len(s)==len(goal) and goal in (s+s)


"""
T.C -> O(n^2) searching in (s+s)
S.C -> O(n) create new string of length (2n)
Approach: String Concatenation + Substring Search

"""
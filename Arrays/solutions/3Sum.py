# https://leetcode.com/problems/3sum/

# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
        
#         n = len(nums)

#         triplet = set()
#         for i in range(n):
#             for j in range(i+1,n):
#                 for k in range(j+1,n):
#                     if (nums[i]+nums[j]+nums[k]==0):
#                         triplet.add(tuple(sorted([nums[i],nums[j],nums[k]])))
        
        
#         triplet = [list(x) for x in triplet]
#         return triplet

"""
Gives TLE Error

T.C -> O(n^3)
S.C -> O(n)

Approach: 
Brute Force Approach (Three Nested Loops + Set for Duplicate Removal)

"""

# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
        
#         n = len(nums)
#         set_nums = set(nums)

#         triplet = set()
#         for i in range(n):
#             temp_set = set()
#             for j in range(i+1,n):
#                 third_val = 0 - (nums[i] + nums[j])
#                 if third_val in temp_set:
#                     triplet.add(tuple(sorted([nums[i],nums[j],third_val])))
#                 temp_set.add(nums[j])
        
        
#         triplet = [list(x) for x in triplet]
#         return triplet
        
"""
T.C -> O(n^2)
S.C -> O(n) + O(no. of tripet)
Approach: 
Hash Set / Hashing Approach (Two Nested Loops + Complement Lookup)

"""
        

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(n):
            if (i!=0 and nums[i]==nums[i-1]):
                continue
            
            j = i+1
            k = n-1
            
            while (j<k):

                total_sum = nums[i]+nums[j]+nums[k]

                if (total_sum<0):
                    j += 1
                elif (total_sum>0):
                    k -= 1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1

                    while (j<k and nums[j]==nums[j-1]):
                        j += 1
                    
                    while (j<k and nums[k]==nums[k+1]):
                        k -= 1
        
        return ans

"""
T.C -> O(n^2)
S.C -> O(1) explicit auxiliary space when the returned answer is excluded. 

Approach: 
Sorting + Two-Pointer Approach (with Duplicate Skipping)

"""
# https://leetcode.com/problems/longest-consecutive-sequence/

# class Solution:
#     def longestConsecutive(self, nums: list[int]) -> int:
#         n = len(nums)
#         if n == 0:
#             return 0

#         nums.sort()
        
#         count = 1
#         max_count = 1
#         for i in range(n-1):
#             diff = nums[i+1] - nums[i]
#             if diff <= 1:
#                 if diff == 1:
#                     count += 1
#                     max_count = max(max_count, count)  
#                 else:
#                     continue                              
                
#             else:
#                 count = 1    
                
        
#         return max_count           

"""

T.C -> O(nlogn)
S.C -> O(n) ; nums.sort() Python uses Timsort, 
which can require up to \(O(n)\) temporary auxiliary space in the worst case.

Approach: 
1. Sort the array in ascending order.
2. Traverse the sorted array and calculate the difference
   between adjacent elements.
3. If the difference is 1, extend the current consecutive sequence.
4. If the difference is 0, skip the duplicate without
   resetting the count.
5. If the difference is greater than 1, reset the count to 1.
6. Keep track of the maximum sequence length.

"""



class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums) #type: ignore
        max_count = 0

        for x in nums:
            if x-1 not in nums:
                
                count = 1
                current = x
                while current+1 in nums:
                    current += 1
                    count += 1

                max_count = max(max_count,count)

        return max_count
        
"""

T.C -> O(n); For creating set, x-1 not in nums takes in set only O(1)
S.C -> O(n); For storing n sets of elements

Approach: Hash Set + Sequence Start Detection

"""
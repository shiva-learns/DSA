# https://leetcode.com/problems/rotate-array/
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(k):
        #     x = nums.pop()
        #     nums.insert(0,x)
        
        def reverse(start,end):
            while (start<end):
                nums[start],nums[end] = nums[end],nums[start]
                start += 1
                end -= 1
        n = len(nums)
        k = k%n
        
        reverse(0, n - 1)    
        reverse(0, k - 1)
        reverse(k,n-1)

"""
T.C -> O(n/2) + O(k/2) + O(n-k/2) = O(n)
S.C -> O(1)
Approach: • Reverse all elements → reverse first k elements → reverse remaining elements.

"""
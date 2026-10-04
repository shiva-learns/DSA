# https://www.geeksforgeeks.org/problems/palindromic-array-1587115620/1?utm=codolio

class Solution:
    def isPalinArray(self, arr):
         # code here
         
        def palindromes(num):
            num_str = str(num)
            n = len(num_str)
            
            for i in range(n//2):
                if num_str[i] != num_str[-1*(i+1)]:
                    return False
            return True
        
        for x in arr:
            if not palindromes(x):
                return False
        return True
                
"""
T.C -> O(n.d)
S.C -> O(1)

Approach: String Conversion + Two-Pointer Technique

"""
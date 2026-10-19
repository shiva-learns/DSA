# https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1
# class Solution:
#     def findUnion(self, a, b):
#         # code here 
        
#         n,m = len(a),len(b)
#         i,j=0,0
        
#         res = []
        
#         while (i<n and j<m):
#             if a[i]<=b[j]:
#                 res.append(a[i])
#                 i += 1
#             else:
#                 res.append(b[j])
#                 j += 1
        
        
#         if (i!=n):
#             res.extend(a[i:])
#         if (j!=m):
#             res.extend(b[j:])
#         new_list = {}
        
#         for x in res:
#             if x not in new_list:
#                 new_list[x] = 1
#         # print(list(new_list.keys()))
        
        
#         return list(new_list.keys())
        


"""
T.C -> O(n+m)
S.C -> O(n+m)


"""

class Solution:
    def findUnion(self, a, b):
        # code here 
        
        n,m = len(a),len(b)
        i,j=0,0
        
        res = []
        
        while (i<n and j<m):
            if a[i]<=b[j]:
                if len(res) == 0 or res[-1] != a[i]:
                    res.append(a[i])
                i += 1
            else:
                if len(res) == 0 or res[-1] != b[j]:
                    res.append(b[j])
                j += 1
        
        
        while i < n:
            if len(res) == 0 or res[-1] != a[i]:
                res.append(a[i])
            i += 1
            
        while j < m:
            if len(res) == 0 or res[-1] != b[j]:
                res.append(b[j])
            j += 1
        
        return res
        
"""
TC -> O(n+m)
SC -> O(n+m)
Approach: Using merge Sort Algorithm


"""
 
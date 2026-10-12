
# https://www.geeksforgeeks.org/problems/merge-sort/1?utm=codolio        
    
    
def merge_array(left,right):
    
    n,m = len(left),len(right)
    result = []
    
    i,j = 0,0
    
    while (i<n) and (j<m):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
    
    if (i<n):
        while (i<n):
            result.append(left[i])
            i += 1
    
    if (j<m):
        while (j<m):
            result.append(right[j])
            j += 1
    return result
    
    
class Solution:
    def mergeSort(self, arr, l, r):
        if (l>=r):
            return [arr[l]]
        
        mid = (l+r)//2
        
        left_sorted=self.mergeSort(arr, l, mid)
        right_sorted=self.mergeSort(arr, mid + 1, r)
        merged = merge_array(left_sorted, right_sorted)

        arr[l:r+1] = merged
        return merged



"""

T.C -> O(nlogn)
S.C -> O(n)
Approach: Merge Sort Inplace

"""
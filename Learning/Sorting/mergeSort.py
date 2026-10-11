
def merge_array(left,right):
    result = []
    i,j = 0,0
    n,m = len(left), len(right)
    while (i<n) and (j<m):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    if i<n:
        while (i<n):
            result.append(left[i])
            i += 1
    
    if j < m:
        while(j<m):
            result.append(right[j])
            j += 1
    
    return result
            
            
            
            
def merge_sort(arr):
    if len(arr) <= 1: # Further we can split the array
        return arr 
    
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    
    return merge_array(left,right)

"""

T.C -> O(nlogn)
S.C -> O(n)

"""

            
            
            
            
            
            
            
            
            
            
            
            
            
            
if __name__=="__main__":
    mylist = [75,29,83,42,16,90,56,34,20,71,88,92,7]
    print(merge_sort(mylist))
    print(mylist)

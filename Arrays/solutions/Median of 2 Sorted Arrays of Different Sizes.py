# https://www.geeksforgeeks.org/problems/median-of-2-sorted-arrays-of-different-sizes/1

# def medianOf2(a,b):
#     j =  0
#     n = len(b)
#     m = len(a)
#     for i in range(n):
        
#         while (j <= n+m):
            
#             if j <= m-1:
#                 if b[i] < a[j]:
#                     a.insert(j,b[i])
#                     break
#             else:
#                 a.append(b[i])
#                 break
#             j += 1
   
#     print(a,len(a))
#     mid = len(a)//2
#     if (len(a)) % 2 != 0:
#         return a[mid]
#     else:
#         return (a[mid-1] + a[mid])/2

""" Above one gives wrong"""

def getMedian(arr):
        mid = len(arr)//2
        if (len(arr)) % 2 != 0:
            return arr[mid]
        else:
            return (arr[mid-1] + arr[mid])/2
    
# def medianOf2(a,b):
        
#     c = a + b
#     c.sort()
#     return getMedian(c)

"""

T.C -> O(n+m log (n+m))
S.C -> O(n+m)
Approach: Using Sorting

Next Approach : Using Merge Sort

"""


# def medianOf2(a,b):
#     n,m = len(a),len(b)
#     c = []
    
#     i,j = 0,0    
#     while (i<=n-1 and j<=m-1):
#         if a[i] < b[j]:
#             c.append(a[i])
#             i += 1
#         else:
#             c.append(b[j])
#             j += 1
    
#     if (j<m):
#         c.extend(b[j:])
#     elif (i<n):
#         c.extend(a[i:])
    
#     print(c)
#     return getMedian(c)
    

"""
T.C -> O(n+m)
S.C -> O(n+m)

"""
    

def medianOf2(a,b):
    n,m = len(a),len(b)
    
    
    i,j = 0,0    
    m1 = -1
    m2 = -1
    
    for _ in range((n+m)//2+1):
        m2 = m1
        
        
        if (i!=n and j!=m):
            if a[i] < b[j]:
                m1 = a[i]
                i += 1
            else:
                m1 = b[j]
                j += 1
        
        elif i<n:
            m1 = a[i]
            i += 1
        else:
            m1 = b[j]
            j += 1
        
    if (n+m)%2 == 1:
        return m1
    else:
        return (m1+m2)/2
        

"""
T.C -> O(n+m)
S.C -> O(1)

"""



if __name__=="__main__":
    a =  [1,2]
    b = [3,4]
    result = medianOf2(a,b)
    print(result)
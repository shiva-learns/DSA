def Max_min_diff(arr):
    arr.sort()
    n = len(arr)
    
    mid = n//2       
    min_sum = 0
    max_sum = 0
    
    j = n-1
    for i in range(mid):
       min_sum += (abs(arr[2*i]-(2*i+1))) 
       max_sum += (abs(arr[i]-arr[j]))
       j -= 1
       
    return min_sum, max_sum



if __name__=="__main__":
    arr = [12,5,25,10,2,15,8,30]
    min_sum,max_sum = Max_min_diff(arr)
    print("Minimum Difference:",min_sum,"\nMaximum Sum:",max_sum)
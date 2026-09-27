def getMinDiff(arr, k):
    # code here
    
    arr.sort()
    return arr

if __name__=="__main__":
    arr = [1, 8, 10, 6, 4, 6, 9, 1]
    k = 7
    print(getMinDiff(arr,k))
def fractional_knapsack(price,item_wt,capacity):
    n = len(item_wt)
    
    items = [(price[i],item_wt[i],price[i]/item_wt[i]) for i in range(n)]
    items.sort(key = lambda x: x[-1],reverse=True)
    print(items)
    
    # i = 0
    profit = 0
    # while (capacity > 0):
    for i in range(n):
        if capacity == 0:
            break
        
        if (capacity - items[i][1] >= 0):
            capacity = capacity - items[i][1]
            profit += items[i][0]
        else:
            profit += (items[i][2]*capacity)
            capacity = 0
            break
    
    
    return profit

if __name__=="__main__":
    price = [21,24,12,40,30]
    item_wt = [3,4,6,5,6]
    capacity = 20
    profit = fractional_knapsack(price,item_wt,capacity)
    print('Total Profit:',profit)
    
    # val = [60,100,120]
    # wt = [10,20,30]
    # capacity = 50
    # print(fractional_knapsack(val,wt,capacity))

"""
T.C -> O(nlogn)
S.C -> O(n)

Approach: Greedy Algorithm

"""
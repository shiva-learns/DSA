# https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1

class Solution:
    def fractionalKnapsack(self, price, item_wt, capacity):
        #code here
        n = len(item_wt)

        items = [(price[i],item_wt[i],price[i]/item_wt[i]) for i in range(n)]
        items.sort(key = lambda x: x[-1],reverse=True)

        profit = 0
        for i in range(n):
            if (capacity==0):
                break

            if (capacity - items[i][1] >= 0):
                capacity = capacity - items[i][1]
                profit += items[i][0]
            else:
                profit += (items[i][2]*capacity)
                capacity = 0
                break

        return profit

"""
T.C -> O(nlogn)
S.C -> O(n)

Approach: Greedy Algorithm

"""
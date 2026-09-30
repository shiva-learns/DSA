def Min_Coin_Change(coins,amount):
    coins.sort()
    
    coin = 0 
    j = len(coins)-1
    while (amount > 0):
        if (amount - coins[j] >= 0):
            amount -= coins[j]
            coin += 1
        else:
            j -= 1
    return coin   



if __name__=="__main__":
    coins = [2,1,5,20,10,50,500,100]
    amount = 1024
    min_coin = Min_Coin_Change(coins,amount)
    print("Minimum Coin:",min_coin)
    
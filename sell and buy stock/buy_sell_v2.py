def buysell2(prices):
    maxprofit = 0
    transactions = 0
    for i in range(0,len(prices) -1 ):
        if prices[i+1] > prices[i]:
            maxprofit += prices[i+1] - prices[i]
            

    return maxprofit

prices = [1,2,3,4,5]
print(buysell2(prices))
def buysell2(prices):
    maxprofit = 0
    minprice = prices[0]
    a = 0
    for i in range(1, len(prices)):
        maxprofit = max(maxprofit, prices[i] - minprice)
        minprice = min(minprice, prices[i])
        print(maxprofit, minprice,a)
        a += 1
    return maxprofit

prices = [7,1,5,3,6,4]
print(buysell2(prices))
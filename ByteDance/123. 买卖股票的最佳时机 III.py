'''
股票买入时机，限制最多两次。
四个变量，分别表示第一次买完，第一次卖完，第二次买完，第二次卖完后手上的钱。

那么转移就很好写了，每次操作完都要保证手上的钱最多，
对于任意一天考虑四个变量:
fstBuy: 在该天第一次买入股票可获得的最大收益
fstSell: 在该天第一次卖出股票可获得的最大收益
secBuy: 在该天第二次买入股票可获得的最大收益
secSell: 在该天第二次卖出股票可获得的最大收益
分别对四个变量进行相应的更新, 最后secSell就是最大
收益值(secSell >= fstSell)
'''
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    fstBuy=-2147483648
    secBuy=-2147483648
    fstSell = 0
    secSell = 0
    for i in range(len(prices)):
        fstBuy = max(fstBuy,-prices[i])
        fstSell = max(fstSell,prices[i] + fstBuy) #fstBuy是负收益
        secBuy = max(secBuy,fstSell - prices[i])
        secSell = max(secSell,secBuy+prices[i])
    return secSell

print(maxProfit([3,3,5,0,0,3,1,4]))
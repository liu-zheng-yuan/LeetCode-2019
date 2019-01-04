#因为能买卖多次 只要当明天的价格比今天高就今天买 明天卖
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_profit = 0
    for i in range(len(prices)-1):
        if prices[i+1] - prices[i] > 0:
            max_profit += prices[i+1] - prices[i]
    return max_profit


print(maxProfit([7,1,5,3,6,4]))
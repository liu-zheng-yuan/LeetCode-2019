def maxProfit( prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    #第1天买 第三天卖可以拆分成 第一天买 第二天卖 第二天买 第三天卖，
    #数组t记录prices[i] - prices[i-1]的值
    t = [0]
    for i in range(1,len(prices)):
        t.append(prices[i] - prices[i-1])
    #在t基础上求最大子序列和.dp[i]为以i结尾的子序列的最大和
    dp = [0] * (len(prices)+1)
    dp[0] = t[0]
    for i in range(1,len(prices)):
        if dp[i-1] + t[i] > t[i]:
            dp[i] = dp[i-1] + t[i]
        else:
            dp[i] = t[i]
    return max(dp)
def maxProfit2( prices:list):
    #记录下第i个价格前最小的价格。以当前价格减去之前最小的价格，就能知道以当前价格卖出所能获得的最高利润
    min_price = 2147483647
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        if max_profit < prices[i] - min_price:
            max_profit = prices[i]- min_price
    return max_profit
print(maxProfit2([7,1,5,3,6,4]))
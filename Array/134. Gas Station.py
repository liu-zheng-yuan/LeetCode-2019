def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    '''O(n2) 超时
    n=len(gas)
    nowTank=0
    rest=0
    i=0
    while i < n:
        for j in range(n+1):# 模拟从i开始走j个加气站
            nowTank=rest + gas[(i+j)%n]
            if nowTank >= cost[(i+j)%n]:
                rest=nowTank-cost[(i+j)%n]
                if i==(i+j+1)%n and j!=0:
                    return i
            else:
                break
        nowTank=0
        rest=0
        i+=1

    return -1
    '''
    #O(n)的解法就是求最大字串和 这个题就是变形的求最大字串和
    #从i开始一路加gas[i] 减cost[i] 直到入不敷出（相当于从前面几个点开始的字串之和为负 不可能是最大字串的一部分）
    # 所以从下个点开始 继续加gas[i] 减cost[i]
    if sum(gas) < sum(cost):
        return -1
    i,curr,n=0,0,len(gas)
    start=0
    while i < n:
        curr += gas[i]
        if curr >= cost[i]:
            curr -= cost[i]
        else:
            start=i+1
            curr=0
        i+=1

    return start
if __name__ == '__main__':
    print(canCompleteCircuit([2,3,4],[3,4,3]))
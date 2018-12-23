def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    #模拟大整数运算 记得进位 .
    temp = []
    for j in range(len(num2)):
        y = int(num2[len(num2) - 1 - j])
        jinwei = 0  # 进位的值
        res = []  # num1 乘以 num2的倒数第i个数的结果
        for i in range(len(num1)):
            x = int(num1[len(num1) - 1 - i])
            xy = x * y + jinwei
            if xy >= 10:
                jinwei = xy//10
                res.append(xy % 10)
            else:
                jinwei = 0
                res.append(xy)
        if jinwei != 0: # 最后的剩余进位值要算进去
            res.append(jinwei)
        resNum = 0
        while len(res) != 0:
            resNum = resNum * 10 + res[len(res) - 1]
            res.pop()
        temp.append(resNum * (10 ** j))
    return sum(temp)


print(multiply("9","9"))

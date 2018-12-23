def restoreIpAddresses(s):
    """
    :type s: str
    :rtype: List[str]
    """
    # 等价于从[1,n-1]的范围内选3个数，在这三个数的位置点小数点，看点出来的格式符不符合ip的格式。
    # 设在i处点小数点 == 在i-1和i之间点小数点
    temp = [0, 0, 0]  # 暂存选出来的3个数
    ans = []
    if s == "":
        return []
    # DFS 对于每个数有选和不选两种情况。选的话就把nowk置为index，进入index+1和nowk+1。不选的话，nowK不加，index+1继续遍历
    def DFS(index, nowK):
        # 都是剪枝 保证ip段的长度不能大于3位
        if nowK == 0 and index >= 4:
            return
        if nowK == 1 and index - temp[0] >= 4:
            return
        if nowK == 2 and index - temp[1] >= 4:
            return
        if nowK == 3 and len(s) - temp[2] >= 4:
            return
        if nowK == 3:
            IP = []
            IP.append(s[0:temp[0]])
            IP.append(s[temp[0]:temp[1]])
            IP.append(s[temp[1]:temp[2]])
            IP.append(s[temp[2]:])
            for x in IP:
                if int(x) < 0 or int(x) > 255 or (len(x)>1 and x[0]=="0"):
                    return
            ans.append(".".join(IP))
            return
        if index == len(s) or nowK > 3:
            return
        temp[nowK] = index
        # 选第index个数
        DFS(index + 1, nowK + 1)
        # 不选第index个
        DFS(index + 1, nowK)

    DFS(1, 0)
    return ans


print(restoreIpAddresses("010010"))

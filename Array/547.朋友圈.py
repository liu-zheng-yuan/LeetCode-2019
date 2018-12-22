def findCircleNum(M:list):
    """
    :type M: List[List[int]]
    :rtype: int
    """
    #并查集 实现路径压缩的find 和union
    def find(father:list,x:int):
        a = x
        while a != father[a]:
            a = father[a]
        #a临时保存一下father位置
        while x!=father[x]:
            z = x
            x = father[x]
            father[z] = a
        return a
    def union(father:list,a:int,b:int):
        fatherA=find(father,a)
        fatherB=find(father,b)
        if fatherA!=fatherB:
            father[fatherA] =fatherB
    father = [i for i in range(len(M))] # 初始化father数组 每个人的父节点就是自己
    for row in range(len(M)):
        for col in range(row):
            if M[row][col] == 1:
                union(father,row,col)
    count_list = [] #保存所有朋友圈的父节点
    for i in range(len(father)):
        find(father,i)
    for i in range(len(father)):
        if father[i] not in count_list:
            count_list.append(father[i])
    return len(count_list)
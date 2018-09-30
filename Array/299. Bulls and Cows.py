from collections import Counter


def getHint(secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    A=0
    B=0
    # 先统计每个数字各有几个
    mapSecret={}
    mapGuess={}
    for k,v in enumerate(secret):
        if mapSecret.get(v)==None:
            mapSecret[v]=1
        else:
            mapSecret[v]+=1

    for k,v in enumerate(guess):
        if mapGuess.get(v)==None:
            mapGuess[v]=1
        else:
            mapGuess[v]+=1

    # 中心思想是分别统计同位同数和同数不同位，找出一个同为同数后 map中个数减一
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            A+=1
            mapSecret[secret[i]]-=1
            mapGuess[guess[i]]-=1
    for k in mapSecret:
        if mapGuess.get(k) !=None:
            B+=min(mapGuess[k],mapSecret[k])

    return "{}A{}B".format(A,B)
'''
另一种方法是分别用两个字典S和G的每个数字出现的位置的集合。然后求两个字典中相同数字出现位置集合的交集，就是A的数量。
相同数字的两个集合中元素个数的min 再减去 交集中元素个数 就是同数不同位的个数
'''
if __name__ == '__main__':
    print(getHint("1123","0111"))
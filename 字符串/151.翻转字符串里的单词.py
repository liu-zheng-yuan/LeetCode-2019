def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    # 原地解法是先反转整个字符串.再反转每个单词,再去除多余空格
    l = []  # 清洗之后的单词列表
    i = 0
    while i < len(s):
        if s[i] == " ":
            i += 1
        else:
            left = i
            while i<len(s) and s[i] != " ":
                i += 1
            right = i
            l.append(s[left:right])
    # 下面是标准的反转
    left = 0
    right = len(l) - 1
    while left < right:
        t = l[left]
        l[left] = l[right]
        l[right] = t
        left +=1
        right -= 1
    return " ".join(l)

print(reverseWords("the sky is blue"))

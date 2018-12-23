def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    count = 0
    if strs ==[]:
        return ""
    for j in range(min([len(x) for x in strs])):
        c = strs[0][j]
        flag = 1
        for i in range(len(strs)):
            if strs[i][j] != c:
                flag = 0
                break
        if flag ==1:
            count+=1
        else:
            break

    return strs[0][0:count]

print(longestCommonPrefix(["aca","cba"]))


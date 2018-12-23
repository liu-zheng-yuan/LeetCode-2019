def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """
    #先去除多余的/
    i = 0
    plist = []
    while i < len(path):
        if i+1 < len(path) and path[i] == "/" and path[i] == path[i+1]:
            i +=1
        else:
            plist.append(path[i])
            i+=1
    plist = "".join(plist).split("/") #洗出来是有效的目录名(包括.)的列表。去除了多余/并且去除split出来的空串
    plist = [x for x in plist if x != ""]
    #用list模拟栈
    stack = []
    for i in range(len(plist)):
        if plist[i] != "." and plist[i] !="..":
            stack.append(plist[i])
        elif plist[i] == ".":
            pass
        elif plist[i] == "..":
            if len(stack) != 0:
                stack.pop()
    #拼最后答案 注意最后没有/ 不能用join
    ans = "/"
    for i in range(len(stack)):
        ans += stack[i]
        if i != len(stack) -1:
            ans += "/"
    return ans

print(simplifyPath("/a/./b/../../c/"))
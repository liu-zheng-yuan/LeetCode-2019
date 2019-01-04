# 给定一个入栈序列和一个出栈序列 看出栈序列是不是合法的
# 后出元素中若有先入的元素 必定是逆序的
def isValid(input:list , output:list):
    flag = True
    for i in range(len(output)):
        index = input.index(output[i])
        l1=[] #存在i后面出的，并在i前面入的元素 应该是按逆序的顺序存的
        for j in range(i+1,len(output)):
            if output[j] in input[:index+1]:
                l1.append(output[j])
        l2=[] #存在i前面入的元素 应该是正序的
        for k in range(0,index):
            if input[k] in l1:
                l2.append(input[k])
        if list(reversed(l1)) != l2:
            flag = False
            break
    return flag

print(isValid([1,2,3,4],[3,2,1,4]))
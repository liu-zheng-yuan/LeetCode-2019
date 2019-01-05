'''
给你一个只由字母'A'和'B'组成的字符串s，找一个最长的子串，要求这个子串里面'A'和'B'的数目相等，输出该子串的长度。
dp思想:设置两个数组A,B.第i位保存以第i位结尾的子串中A和B的个数.
遍历A\B数组,当A的数量和B的数量相同时,用两个变量记录此时最长的AB数量.如果下面还有更大的AB数量并满足A数量等于B数量,就更新这两个变量
'''
def maxABSubString(s):
    n = len(s)
    #分别记录以i结尾的子串中A,B的数量
    A = [0] * n
    B = [0] * n
    A[0] = 1 if s[0] == 'A' else 0
    B[0] = 1 if s[0] == 'B' else 0
    for i in range(1,n):
        if s[i] == "A":
            A[i] = A[i-1] + 1
            B[i] = B[i-1] #别忘了 更新另一个B数组
        else:
            B[i] = B[i-1] + 1
            A[i] = A[i - 1]  # 别忘了 更新另一个B数组
    max_A_count = 0
    max_B_count = 0
    for i in range(n):
        if A[i] == B[i]:
            if A[i] > max_A_count:
                # 因为AB数量相等 只要一个变量就行
                max_A_count = A[i]
                max_B_count = B[i]
    #最大的长度就就是A和B出现的次数
    return max_A_count + max_B_count

print(maxABSubString("ABAAABBBA"))
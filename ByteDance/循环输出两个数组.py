'''
 给两个数组（长度可能不等），要求循环输出如
A=1,2,3
B=A,B,C,D,
就要输出1A2B3C1D2A3B...

这个很简单的，维护两个下标变量ai,bi,自增时取模就行了,如
ai = (ai+1)%A.length
要求输出重复时循环跳出

一开始想到最小公倍数去了，面试官提示从下标考虑，当ai与bi相等且为0的时候跳出就行了 这个好像不对
还是要从公倍数考虑.
所谓重复 就是两个数组的头又一次对齐了
即A数组整体输出次数乘以A数组个数  等于  B数组整体输出次数乘以B数组个数
'''
A = [1, 2, 3]
B = ['A', 'B', 'C', 'D']
a = 0
acount = 0
b = 0
bcount = 0
ans = []
flag = True
while True:
    if flag:
        ans.append(A[a])
        a = (a + 1) % len(A)
        if a % len(A) == 0:
            acount += 1
    else:
        ans.append(B[b])
        b = (b + 1) % len(B)
        if b % len(B) == 0:
            bcount += 1
    flag = False if flag == True else True
    if (acount) * len(A) == (bcount) * len(B) and acount != 0 and bcount != 0:
        break
print(ans)

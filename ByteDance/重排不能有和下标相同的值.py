'''
一个数组，每个位置的值对应下标。
重新排列，要求对应位置上不能有同下标相同的值，即原先a[0]=0，重排后a[0]不可以等于0。输出总共有多少种重新排列的方法。
'''
import copy
global ans
ans = []
def recursive(arr: list, n: int, index: int, visited: list):
    if index == n:
        global ans
        # python 浅拷贝的坑 不能直接加入arr 而是加入arr的复制
        ans.append(copy.copy(arr))
        return
    for i in range(n):
        if visited[i] == 0:
            if index != i:
                visited[i] = 1
                arr[index] = i
                recursive(arr, n, index + 1, visited)
                arr[index] = -999 #表示复位 有没有无所谓
                visited[i] = 0


recursive([-999] * 4, 4, 0, [0] * 4)
print(ans)

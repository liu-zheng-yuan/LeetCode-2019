def getPermutation(n, k):
    def recurive(n: int, index: int, l: list, k: int, visited: list):
        if index > n:
            return
        if index == n:
            global nowk
            if nowk == k:
                nowk = k+1
                global ans
                ans =  "".join([str(x) for x in l])
            else:
                nowk += 1

        for i in range(1, n + 1):
            if visited[i] == 0:
                visited[i] = 1
                l[index] = i
                recurive(n, index + 1, l, k, visited)
                visited[i] = 0

    l=[0]*n
    visited = [0] *(n+1)
    global nowk
    nowk = 1
    global ans
    recurive(n,0,l,k,visited)
    return ans



print(getPermutation(9,24))
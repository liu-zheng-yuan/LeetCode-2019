# 如果是无序数组的中位数的话 转化成求第k大数的题--->k等于n+1//2 也就是中位数
# 此题可以将旋转后的数组看成两个有序数组，求两个有序数组的中位数，也就是求第k个小的数。复杂度log（n+m）

#先求出旋转数组的分界点
def cutPoint(arr:list):
    left = 0
    right = len(arr)-1
    while left < right:
        mid = (left+right) //2
        if arr[left] < arr[mid]: #说明arr[left]到arr[mid]递增
            left = mid
        else:
            right = mid
    return left

def midNumber(arr1:list,arr2:list):
    sumNum = len(arr1) + len(arr2)
    k = 0 #中位数的索引值
    isOdd = None
    if sumNum % 2 == 0:
        isOdd = False
        k = sumNum//2
    else:
        isOdd = True
        k = sumNum//2 + 1

arr = [4, 5, 6, 7, 1, 2, 3]
cutpoint = cutPoint(arr)
arr1 = arr[:cutpoint+1]
arr2 = arr[cutpoint:]
print(midNumber(arr1,arr2))

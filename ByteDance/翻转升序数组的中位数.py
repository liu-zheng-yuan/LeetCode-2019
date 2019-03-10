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

#二分查找 找两个升序数组中第k大的数
def Binary_find_Kth(arr1: list, arr2: list, k):
    # 认为len1 < len2
    if len(arr2) < len(arr1):
        arr1, arr2 = arr2, arr1
    # 递归边界
    # 要先判断arr1是不是空了
    if len(arr1) == 0:
        return arr2[k - 1]
    if k == 1:
        return min(arr1[0], arr2[0])


    # 将k分成两部分 分别在arr1和arr2上找
    k1 = min(k // 2, len(arr1))
    k2 = k - k1

    # 说明array2的k2-1前部分一定在第k大元素之前，因此：
    # 1）将k2-1这部分全跳过:更新数组首位地址索引
    # 2）将这k2元素纳入已找到的第k大元素范围内，更新k值：k-k2
    if arr1[k1 - 1] > arr2[k2 - 1]:
        return Binary_find_Kth(arr1, arr2[k2:], k - k2)
    # 说明array1的k1-1前部分一定在第k大元素之前，因此：
    # 1）将k1-1这部分全跳过:更新数组首位地址索引，同时更新数组长度；
    # 2）将这k1元素纳入已找到的第k大元素范围内，更新k值：k-k1
    elif arr1[k1 - 1] < arr2[k2 - 1]:
        return Binary_find_Kth(arr1[k1:], arr2, k - k1)
    else:
        #当array1[k/2-1] == array2[k/2-1] 找到第k个
        return arr1[k1]
def find_mid_number(arr):
    cutpoint = cutPoint(arr)
    #划分为两个升序数组
    arr1 = arr[:cutpoint + 1]
    arr2 = arr[cutpoint+1:]
    #计算中位数是第k大
    if len(arr) % 2 == 1:
        #奇数 中位数只有一个 是k//2+1
        k = len(arr)//2 +1
        return Binary_find_Kth(arr1,arr2,k)
    else:
        #偶数 中位数是k//2 和 k//2+1 两个数的和
        k1 = len(arr)//2
        k2 = len(arr)//2+1
        return (Binary_find_Kth(arr1,arr2,k1)+Binary_find_Kth(arr1,arr2,k2))/2

arr = [4, 5, 6, 7, 1, 2, 3]
print(find_mid_number(arr))

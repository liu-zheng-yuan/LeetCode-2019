'''
一、题目描述

给定两个已经排序好的数组，找到两者所有元素中第k大的元素
二、解法分析
解法一：参照归并排序

    将两个有序数组变成一个有序数组：merge两个数组，然后求第k大的数，时间复杂度O(m+n) 空间m+n

解法二：游标计数
    题目只要求第k大的数，没必要花力气将数组全部再排序，可以定义两个游标分别指向两个有序数组，按序移动，并用count计数，当count等于k时，返回两个游标指向的数中最小的那一个

    时间复杂度O(m+n)

解法三：类二分查找
    充分利用两个数组都是有序的条件：
    1）当array1[k/2-1] == array2[k/2-1] 则返回array1[k/2-1]或者array2[k/2-1]
    2）当array1[k/2-1] > array2[k/2-1]  则array2在[0,k/2-1]范围内的元素一定比array1、array2合并后第k个元素小，可以不用考虑array2在[0,k/2-1]范围内的元素
    3）当array1[k/2-1] < array2[k/2-1]  则array1在[0,k/2-1]范围内的元素一定比array1、array2合并后第k个元素小，可以不用考虑array1在[0,k/2-1]范围内的元素
     因此算法可以写成一个递归的形式，递归结束的条件为：
    1）array1[k/2-1] == array2[k/2-1] return array1[k/2-1]
    2）array1或者array2为空时，return array1[k-1]或者array2[k-1]
    3）k==1时，返回min(array1[0],array2[0])

    时间复杂度O(log(m+n))
'''


def Binary_find_Kth(arr1: list, arr2: list, k):
    # 认为len1 < len2
    if len(arr2) < len(arr1):
        arr1, arr2 = arr2, arr1
    # 递归边界
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

print(Binary_find_Kth([1,2,3,9],[4,5,6],5))
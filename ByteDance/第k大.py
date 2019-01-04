# 1.做k次选择排序
def kChooseSort(arr, k):
    for i in range(k):
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr[k - 1]


# 2.参考快排partition，每做一次把pivot放在正确的位置上，若此位置index大于k，在left到index之间做partition。若此位置小于k，在index到right之间做parttion
def partition(arr: list, left, right):
    pivot = arr[left]
    while left < right:
        while left < right and arr[right] <= pivot:
            right -= 1
        arr[right], arr[left] = arr[left], arr[right]
        while left < right and arr[left] >= pivot:
            left += 1
        arr[right], arr[left] = arr[left], arr[right]
    arr[left] = pivot
    return left


def kPartition(arr, k):   #★ O（n）的
    left = 0
    right = len(arr) - 1
    while left <= right: # 二分查找 left能等于right
        pivot_index = partition(arr,left,right)
        if pivot_index == k - 1:
            return arr[pivot_index]
        elif pivot_index > k-1:
            right = pivot_index-1 #二分查找 要不断-1 +1 缩小
        else:
            left = pivot_index+1
# 3.海量数据TopK
from queue import PriorityQueue
'''
先拿10000个数建小顶堆，然后依次添加剩余元素，如果大于堆顶的数（10000中最小的），将这个数替换堆顶，并调整结构使之仍然是一个最小堆
这样，遍历完后，堆中的10000个数就是所需的最大的10000个。建堆时间复杂度是O（mlogm），算法的时间复杂度为O（nlogm）（n为10亿，m为10000）。

优化的方法：可以把所有10亿个数据分组存放，比如分别放在1000个文件中。
这样处理就可以分别在每个文件的10^6个数据中找出最大的10000个数，合并到一起在再找出最终的结果。
'''
print(kPartition([1, 2, 4, 234, 44, 112, 424], 7))

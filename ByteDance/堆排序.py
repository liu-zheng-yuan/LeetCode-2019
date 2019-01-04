# 将[low,high]数组中low位置的元素放到大顶堆中正确的地方
def downAdjust(heap: list, low: int, high: int):
    parent = low  # 欲调整结点
    child = parent * 2  # i的左孩子

    while child <= high:  # 存在孩子结点
        # 如果右孩子存在且右孩子的值大于左孩子
        if child + 1 <= high and heap[child + 1] > heap[child]:
            child = child + 1  # 让child储存右孩子的下标

        # 如果孩子的权值比父节点大，就要交换
        if heap[child] > heap[parent]:
            heap[child], heap[parent] = heap[parent], heap[child]
            parent = child  # 保持parent为欲调整结点
            child = 2 * parent
        else:
            break  # 孩子的权值均比父节点小 调整结束


# 真正的建堆。从后往前，从第一个非叶子节点开始（n//2）到1号位置，每个都做[i,n]的调整。倒着枚举保证了 每个结点都是以其为根节点的子树中权值最大的结点
def createHeap(heap: list):
    #第0位无意义，所以一共只有len - 1 个数
    for i in range((len(heap)-1) // 2, 0, -1):
        downAdjust(heap, i, len(heap)-1)

# 堆排序。建堆完成之后，每次将堆顶的元素和数组最后的元素交换。然后做调整。
def heapSort(heap:list):
    createHeap(heap)
    for i in range(len(heap)-1,1,-1): #倒着枚举。当堆中还剩一个元素时，就没必要调整了
        heap[i],heap[1] = heap[1],heap[i]
        downAdjust(heap,1,i-1)
    return heap

print(heapSort([-1,85,55,82,57,68,92,99,98,66,56]))
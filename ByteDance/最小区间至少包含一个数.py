'''
其实就是利用归并的思想，三个数组或更多个数组做归并排序，排在最小的元素向前移动，计算最大最小元素之间的间隔,就是区间大小，这样当一个数组用尽的时候，记录的最小间隔即为所求。
'''
'''
解答方法：
初始化大小为k的最小堆，k个数字是每个数组中的最小值，设置变量maxValue记录k个数字中最大值，删除堆顶元素，
将原堆顶元素(也就是现在三个元素中最小的那个)对应的数组中下一个值加入到堆中
调整堆，并且记录当前区间范围（maxValue - minValue），重复执行直到某个数组所有值都被删除。
'''
#这里的堆里的元素是一个二元组,第一个元素是k个数组中的值,第二个元素是这个值属于第几个数组,方便找到对应的指针
# 小顶堆
def downAdjust(heap:list,low,high):
    parent = low
    child = low*2
    while child <= high:
        if child+1 <= high and heap[child+1][0] < heap[child][0]:
            child = child+1
        if heap[parent][0] > heap[child][0]:
            heap[parent],heap[child] = heap[child],heap[parent]
            parent = child
            child = parent*2
        else:
            break
# 堆中第0个无效 从第1个开始
def createHeap(heap:list):
    n = len(heap)
    for i in range((n-1)//2,0,-1):
        downAdjust(heap,i,n-1)

def solve(arrList:list):
    k = len(arrList)
    heap = [(-1,-1)] #堆的第0号位无意义
    maxValue = -2147483648
    min_range_value = 2147483647
    index = [0] * k #记录k个数组上的指针位置 初始都是0
    for i in range(k):
        heap.append((arrList[i][0],i))
        if arrList[i][0] > maxValue:
            maxValue = arrList[i][0]
    #把每个数组第0个元素组成一个K个元素的小顶堆,方便每次查找区间内最大值
    createHeap(heap)

    while True:
        #当前堆中最小的值和这个值所在的数组
        minValue = heap[1][0]
        arrIndex = heap[1][1]
        #找到当前堆中的最大值
        maxValue = max(heap[1:],key=lambda x:x[0])[0]
        #如果当前区间范围小于记录的 就更新
        if maxValue - minValue < min_range_value:
            min_range_value = maxValue - minValue
        #如果有一个数组遍历完了 就返回当前的最小区间
        if index[arrIndex] + 1 >= len(arrList[arrIndex]):
            return (minValue,maxValue)

        #根据现在堆中的最大\最小值,算出当前的min_range_value 然后更新
        #删掉这个最小值
        #找到这个最小值所在数组对应的指针加一位置的值,放入数组
        heap.remove((minValue,arrIndex))
        index[arrIndex] += 1
        nextValue = arrList[arrIndex][index[arrIndex]]
        heap.insert(1,(nextValue,arrIndex))
        downAdjust(heap,1,len(heap)-1)


print(solve([[4, 10, 15, 24, 26],[0, 9, 12, 20],[5, 18, 22, 30]]))
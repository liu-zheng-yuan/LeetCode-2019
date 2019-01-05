'''
## 10.有序数组的二分查找，加了点难度（其实没有难度。。。），找出目标元素第一次出现的位置。

既然是有序的，找到后一直向左边找到第一个不等于该元素的值的位置，然后返回其加一就好了。写出来后还是继续扣鲁棒性。
'''
def binSearchFirst(arr,key):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right) //2
        if key >arr[mid]:
            left = mid + 1 # 因为arr[mid]还小于key 可以放心的加1 缩小范围
        else:
            right = mid  #因为此时key<= arr[mid],可能right处就是key或者right前有很多key 不能盲目减一
            #下边界不动 只动上边界
            #当上下边界相遇 就是第一个key或者是没找到
        if left == right:
            break
    #这里只是找到了left == right 的位置 但并不一定要找的元素存在
    if arr[left] != key:
        return -1
    else:
        return left

def binSearchLast(arr,key):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right) //2
        if key >= arr[mid]:
            left = mid
        else:
            right = mid - 1
        if left == right:
            break
    if arr[left] != key:
        return -1
    else:
        return left

print(binSearchLast([1,2,3,3,4,5],3))
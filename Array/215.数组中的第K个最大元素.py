def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # 1 k 次 选择排序
    # if nums == []:
    #     return 0
    # for i in range(k):
    #     for j in range(i+1,len(nums)):
    #         if nums[i] < nums[j]:
    #             t = nums[j]
    #             nums[j] = nums[i]
    #             nums[i] = t
    # return nums[k - 1]
    # 2 桶排序 当数组里有负数或非整数时不能用
    # 3 快排partition的理念，每次把中间的数放在正确的位置上，如果中间的数的位置小于k，就再排左边的，如果大于k，就排右边的，总的是O（N)
    left = 0
    right = len(nums) - 1
    while left <= right: # ★ 对于二分（这里类似二分查找） while条件中left<=right 但对于双指针(快拍) left < right
        pivot = partition(nums, left, right)
        if pivot == len(nums) - k:
            return nums[pivot]
        elif pivot < len(nums) - k:
            left = pivot + 1
        elif pivot > len(nums) - k:
            right = pivot - 1


# 就是快排里的划分函数 把pivot排在正确的位置上,并且在数组“大致的中间” 返回排好后的pivot的索引
def partition(nums: list, left: int, right: int):
    pivot = nums[left]
    if left >= right:
        return 0
    while left < right:
        while left < right and nums[right] >= pivot:
            right -= 1
        if left < right:
            nums[left] = nums[right]
        while left < right and nums[left] <= pivot:
            left += 1
        if left < right:
            nums[right] = nums[left]
    # 停下来的地方就是pivot 应该在的地方
    nums[left] = pivot
    return left


print(findKthLargest([2, 1], 2))

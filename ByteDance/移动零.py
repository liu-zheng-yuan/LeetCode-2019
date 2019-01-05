def moveZeroes(nums):
    """
    :type nums: List[int]
    """
    slow = 0  # 慢指针 也就是统计非0元素个数的计数器
    fast = 0  # 快指针 统计所有元素个数
    for i in range(len(nums)):
        fast += 1
        if nums[i] != 0:
            nums[slow] = nums[i]
            slow += 1
    for i in range(fast - slow):
        nums.pop()

    for i in range(fast - slow):
        nums.append(0)
moveZeroes([0,1,0,3,12])


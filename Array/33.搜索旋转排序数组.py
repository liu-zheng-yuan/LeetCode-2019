def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(nums) - 1
    while (left <= right):
        mid = (left + right) // 2  # py地板除法 是 //
        if nums[mid] == target:
            return mid
        if nums[mid] > nums[right]:  # [left,mid]递增
            if target < nums[mid] and target >= nums[left]:  # 这里写什么情况下要去递增的区间搜搜
                right = mid - 1
            else:  # 除了上面那一种情况 其他都是去不递增的区间搜索
                left = mid + 1
        else:  # nums[mid] < nums[right] [mid ,right] 递增 或者当找不到这个数的时候 mid == right 能进入这个else 然后right-1能退出while
            if target > nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


print(search([4, 5, 6, 7, 0, 1, 2], 3))
